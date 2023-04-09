from pywebcopy import save_website
import csv
with open('ready_domains.csv', 'r') as f_csv:
    domains = csv.reader(f_csv)
    for name_url_ in domains:
        name_url = name_url_[0]
        save_website(
                    url=name_url,
                    project_folder="websites://savedpages//",
                    project_name=name_url.split('/')[2],
                    threaded=True
                )
