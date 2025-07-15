
def send_capacity_alert():
    from frappe.utils import add_days, nowdate
    sessions = frappe.get_all("Course Session", filters={"session_date": add_days(nowdate(), 2)}, fields=["name", "session_date", "capacity"])
    for s in sessions:
        total = s.capacity
        filled = frappe.db.count("Course Session Attendance", {"session": s.name})
        if filled >= total * 0.8:  # Alert at 80% filled
            template = frappe.render_template("templates/email/session_capacity_alert.html", {
                "session_name": s.name,
                "session_date": s.session_date,
                "filled_seats": filled,
                "total_capacity": total
            })
            frappe.sendmail(
                recipients=["admin@example.com"],
                subject="Session Nearly Full",
                message=template
            )
