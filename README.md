# Frappe Dation LMS

This is the extended Frappe LMS app configured for Dation's multi-tenant use case.

## 🚀 Setup Instructions

### 1. Clone and Setup Bench
```bash
git clone https://github.com/frappe/bench bench-repo
cd bench-repo
pip install -e .
bench init dation-bench --frappe-branch version-15
cd dation-bench
```

### 2. Create Site
```bash
bench new-site dation.local
```

### 3. Get LMS and This App
```bash
bench get-app frappe_lms https://github.com/frappe/lms
bench get-app frappe_dation_lms /home/frappe/frappe_dation_lms
```

> Adjust path above if different

### 4. Install Apps
```bash
bench --site dation.local install-app frappe_lms
bench --site dation.local install-app frappe_dation_lms
```

### 5. Start Development Server
```bash
bench start
```

## 🧾 Certificate
Edit `certificate_template.html` to apply your custom branding and design.

## 🐳 Docker
Use the included `Dockerfile` to run this app in a containerized environment.

## 🧠 Notes
- This setup includes custom dashboards, API endpoints, role permissions, server scripts, and automation for notifications and course handling.
- Make sure to run `bench migrate` after pulling new changes.

Enjoy your LMS!

## 🎨 Branding per Educator or Company
- Use `/branding/theme.css` to customize global color scheme
- Dynamic logos and brand titles can be injected in context via templates or scripts
- You can extend each DocType (Educator, Company) to include `logo`, `brand_color`, and load them accordingly


## 🧩 Custom Fields
You can install the branding fields via:

```bash
bench --site [yoursite] execute frappe.desk.doctype.custom_field.custom_field.create_custom_fields "custom_fields/educator_extension.json"
```
