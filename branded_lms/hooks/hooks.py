app_name = "branded_lms"
app_title = "Branded LMS"
app_publisher = "Curious Inc."
app_description = "Custom theming and branding for LMS"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@curious-inc.com"
app_license = "MIT"

fixtures = ["Custom Field", "Property Setter","Role", "User Permission", "Custom DocPerm"]
doc_events = {
    "Course Enrollment": {
        "on_submit": "branded_lms.api.lms_api.on_course_enrollment_submit"
    }
}
