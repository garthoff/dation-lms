FROM frappe/bench:latest

COPY . /home/frappe/frappe_dation_lms

WORKDIR /home/frappe/frappe_dation_lms

RUN bench get-app frappe_dation_lms . && \
    bench --site dation.local install-app frappe_dation_lms