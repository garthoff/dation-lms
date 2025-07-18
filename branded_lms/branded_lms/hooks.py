app_name = "branded_lms"
app_title = "Branded LMS"
app_publisher = "Your Company"
app_description = "LMS integration for Dation & Educators"
app_version = "1.5.0"
app_license = "MIT"

# Minimal fixtures
fixtures = ["Role"]

# Only working routes - NO missing files
website_route_rules = [
    {"from_route": "/test-basic", "to_route": "test-basic"}
]

# NO custom assets for now
# app_include_css = ""
# app_include_js = ""

# Minimal doc events
doc_events = {
    "Course Enrollment": {
        "on_update": "branded_lms.course_hooks.check_completion_and_send_email"
    }
}