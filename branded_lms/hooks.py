

# Course completion hook
doc_events = {
    'Course Enrollment': {
        'on_update': 'branded_lms.course_completion_hooks.on_course_complete'
    }
}
