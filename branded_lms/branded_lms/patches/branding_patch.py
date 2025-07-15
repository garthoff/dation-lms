def execute():
    import frappe
    if not frappe.db.exists("Custom Field", "Educator-branding_color"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Educator",
            "fieldname": "branding_color",
            "fieldtype": "Color",
            "label": "Branding Color"
        }).insert()
