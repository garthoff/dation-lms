from . import __version__ as app_version

app_name = "branded_lms"
app_title = "Branded LMS"
app_publisher = "Your Company"
app_description = "LMS integration for Dation & Educators"
app_icon = "octicon octicon-zap"
app_color = "grey"
app_email = "info@yourcompany.com"
app_license = "MIT"

# Includes in <head>
# Use the built CSS bundle generated via build.json
app_include_css = "/assets/branded_lms/css/branded_lms.css"
# Use the JavaScript bundle defined in build.json
app_include_js = "/assets/branded_lms/js/branded_lms.js"

# Fixtures (include all custom DocTypes, roles, permissions)
fixtures = [
    "Custom Field",
    "Property Setter",
    "Custom Script",
    "Server Script",
    "Workflow",
    "Role",
    "Email Template",
    "Client Script",
    "Report",
    "Dashboard Chart",
    "Notification",
    {"dt": "Portal Menu Item", "filters": [["module_name", "=", "Branded LMS"]]},
]

# Website Routes
website_routes = [
    {"from_route": "/my-courses", "to_route": "branded_lms.www.my_courses"},
    {"from_route": "/dashboard", "to_route": "branded_lms.www.dashboard"},
    {"from_route": "/dashboard", "to_route": "branded_lms.www.dashboard"},{
        "from_route": "/dl/hr_manager_dashboard",
        "to_route": "hr_manager_dashboard"
    },
    {
        "from_route": "/dl/educator_dashboard",
        "to_route": "educator_dashboard"
    },
    {
        "from_route": "/dl/student_dashboard",
        "to_route": "student_dashboard"
    },
    {
        "from_route": "/dl/company_dashboard",
        "to_route": "company_dashboard"
    },    
    {
        "from_route": "/test-basic",
        "to_route": "test-basic"
    },
]

# Portal Setup
portal_menu_items = [
    {"title": "Dashboard", "route": "/dashboard", "role": "Student"},
    {"title": "My Courses", "route": "/my-courses", "role": "Student"},
]

# Permissions via role
permission_query_conditions = {
    "Course Enrollment": "branded_lms.doctype.course_enrollment.course_enrollment.get_permission_query_conditions",
}
has_permission = {
    "Course Enrollment": "branded_lms.doctype.course_enrollment.course_enrollment.has_permission",
}

# Email Templates
email_templates = {
    "course_enrollment": "branded_lms/templates/email/course_enrollment.html",
    "course_completion": "branded_lms/templates/email/course_completion.html",
    "class_reminder": "branded_lms/templates/email/class_reminder.html",
}

# Server Scripts
doc_events = {
    "Course Enrollment": {
        "on_update": "branded_lms.course_hooks.check_completion_and_send_email"
    },
    "Course Session": {
        "on_update": "branded_lms.session_hooks.send_capacity_warning"
    },
    "User": {
        "after_insert": "branded_lms.api.user_hooks.assign_roles_automatically"
    }
}

# Scheduled Tasks
scheduler_events = {
    "daily": [
        "branded_lms.api.notifications.send_reminders_for_upcoming_sessions"
    ]
}

# Override Methods (if needed)
# override_whitelisted_methods = {
#     "frappe.desk.search.search_link": "branded_lms.api.custom_search.search_link"
# }

# After Install Script (e.g., preload roles, templates)
after_install = "branded_lms.install.setup_defaults"
