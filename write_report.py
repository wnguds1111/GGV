
# Write the complete HTML report to file
html = open('gnjoy_billing_complete_report_template.html', 'r', encoding='utf-8').read()
open('gnjoy_billing_complete_report.html', 'w', encoding='utf-8').write(html)
print("Done")
