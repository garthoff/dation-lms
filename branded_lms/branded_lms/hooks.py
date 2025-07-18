from . import __version__ as app_version

app_name = "branded_lms"
app_title = "Branded LMS"
app_publisher = "Your Company"
app_description = "LMS integration for Dation & Educators"
app_icon = "octicon octicon-zap"
app_color = "grey"
app_email = "info@yourcompany.com"
app_license = "MIT"

app_include_js = "/assets/branded_lms/js/branded_lms.js"
app_include_css = "/assets/branded_lms/css/branded_lms.css"

# Fixtures (include all custom DocTypes, roles, permissions)
fixtures = [

]

# Website Routes
website_routes = [

]

# Portal Setup
portal_menu_items = [

]

# Permissions via role
permission_query_conditions = {
}
has_permission = {
}

# Email Templates
email_templates = {

}

# Server Scripts
doc_events = {

}

# Scheduled Tasks
scheduler_events = {

}

# After Install Script (e.g., preload roles, templates)
after_install = "branded_lms.install.setup_defaults"
