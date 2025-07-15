import frappe


def setup_defaults():
    """Create initial settings required after installation."""
    # Example: ensure default roles or workflows exist
    frappe.log_error("Setting up Branded LMS defaults", "install")
