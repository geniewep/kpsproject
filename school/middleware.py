from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse, NoReverseMatch


class InsertNavMiddleware(MiddlewareMixin):
    """Inject a simple navigation bar before </body> for all HTML responses.

    Links are generated using Django's `reverse()` so they stay correct if
    URL patterns are renamed. If a name cannot be reversed, the link falls
    back to '#' to avoid broken anchors.
    """

    LINKS = [
        ("Admin (Light)", 'admin_dashboard_light'),
        ("Admin (Dark)", 'admin_dashboard_dark'),

        ("Teacher (Light)", 'teacher_dashboard_light'),
        ("Teacher (Dark)", 'teacher_dashboard_dark'),

        ("Parent (Light)", 'parent_dashboard_light'),
        ("Parent (Dark)", 'parent_dashboard_dark'),

        ("Attendance (Light)", 'attendance_teachers_light'),
        ("Attendance (Dark)", 'attendance_teachers_dark'),

        ("Grading (Light)", 'grading_marks_entry_light'),
        ("Grading (Dark)", 'grading_marks_entry_dark'),

        ("Messaging (Light)", 'messaging_interface_light'),
        ("Messaging (Dark)", 'messaging_interface_dark'),

        ("Student (Light)", 'student_profile_light'),
        ("Student (Dark)", 'student_profile_dark'),

        ("Reports", 'report_generation_for_admin'),
        ("Announcements", 'school_wide_announcements'),
        ("User Management", 'user_management'),
        ("Settings", 'system_settings'),
        ("Calendar", 'calendar'),
    ]

    NAV_WRAPPER_START = (
        '<nav id="site-nav" '
        'style="position:fixed;bottom:12px;right:12px;z-index:9999;background:rgba(255,255,255,0.95);border:1px solid #ddd;padding:10px;'
        'border-radius:8px;box-shadow:0 6px 24px rgba(0,0,0,0.12);'
        'font-family:system-ui,Segoe UI,Roboto,Arial,sans-serif;font-size:14px">'
        '<strong style="display:block;margin-bottom:6px">Quick Links</strong>'
        '<div style="display:flex;gap:8px;flex-wrap:wrap;max-width:420px">'
    )

    NAV_WRAPPER_END = '</div></nav>'

    def build_nav(self, request):
        parts = []
        for label, name in self.LINKS:
            try:
                url = reverse(name)
            except NoReverseMatch:
                url = '#'
            parts.append(f'<a href="{url}">{label}</a>')
        return self.NAV_WRAPPER_START + ''.join(parts) + self.NAV_WRAPPER_END

    def process_response(self, request, response):
        try:
            content_type = response.get('Content-Type', '')
            if response.status_code == 200 and 'text/html' in content_type.lower():
                content = response.content.decode(response.charset or 'utf-8')
                lower = content.lower()
                if '</body>' in lower:
                    idx = lower.rfind('</body>')
                    # Use original content slice to preserve original casing
                    nav_html = self.build_nav(request)
                    new_content = content[:idx] + nav_html + content[idx:]
                    response.content = new_content.encode(response.charset or 'utf-8')
                    if response.get('Content-Length', None):
                        try:
                            response['Content-Length'] = str(len(response.content))
                        except Exception:
                            pass
        except Exception:
            # Don't let nav injection break the site; fail silently
            pass
        return response
