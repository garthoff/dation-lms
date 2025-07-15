#!/bin/bash

echo "🚀 Setting up Frappe Dation LMS"

bench get-app --branch version-15 frappe_dation_lms https://github.com/your-org/frappe_dation_lms.git
bench new-site dation-lms.local --install-app frappe_dation_lms --admin-password admin --mariadb-root-password root
bench --site dation-lms.local execute frappe.desk.doctype.desktop_icon.desktop_icon.setup_icons
bench --site dation-lms.local export-fixtures --app frappe_dation_lms
bench --site dation-lms.local migrate
bench --site dation-lms.local clear-cache