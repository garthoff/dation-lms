
def generate_certificate(enrollment):
    from frappe.model.document import Document
    from frappe.utils.pdf import get_pdf
    from frappe import render_template, sendmail

    enrollment_doc = frappe.get_doc("Course Enrollment", enrollment)
    student = frappe.get_doc("Student", enrollment_doc.student)
    course = enrollment_doc.course
    template = frappe.get_all("Certificate Template", filters={
        "used_by": "Educator",
        "used_by_id": enrollment_doc.educator
    }, fields=["html_content"], limit=1)

    if not template:
        # fallback to default template
        template = frappe.get_all("Certificate Template", filters={
            "used_by": "Dation"
        }, fields=["html_content"], limit=1)

    html = render_template(template[0]["html_content"], {
        "student_name": student.full_name,
        "course": course,
        "completion_date": enrollment_doc.completion_date
    })
    pdf = get_pdf(html)

    # Optional: email PDF
    sendmail(
        recipients=[student.email],
        subject="Your Course Certificate",
        message="Find your certificate attached.",
        attachments=[{
            "fname": f"Certificate_{student.full_name}.pdf",
            "fcontent": pdf
        }]
    )
