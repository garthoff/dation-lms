# Frappe Dation LMS

This app extends Frappe LMS to support Educators, Companies, Students, HR Teams, Creators, Instructors, and Multi-tenant workflows for a B2B e-learning SaaS.

## 🧱 Installation

```bash
bench get-app frappe_dation_lms https://github.com/your-org/frappe_dation_lms.git
bench new-site dation-lms.local
bench --site dation-lms.local install-app frappe_dation_lms
```

## 🚀 Fixtures Included
- Custom DocTypes
- Role Permissions
- Sample Data
- Dashboards & Charts
- Server Scripts
- Certificate Templates
- Notifications

## 🧪 Development Use
```bash
bench --site dation-lms.local execute frappe.desk.doctype.desktop_icon.desktop_icon.setup_icons
bench --site dation-lms.local export-fixtures --app frappe_dation_lms
```

## 📦 Demo Logins (after setup)
- HR Manager: hr@fleetcorp.nl / demo
- Educator Admin: admin@drivepro.com / demo