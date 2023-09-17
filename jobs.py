import os

def joblist():
    CACHE_PATH = os.path.join(os.getcwd(), 'static', 'cached_joblist.txt')

    try:
        with open(CACHE_PATH, 'r') as cache_file:
            cached_joblist = cache_file.read()
            dropdown_options = ""
            for job_name in cached_joblist.split(','):
                dropdown_options += f"<option value='{job_name}'>{job_name}</option>"
            return dropdown_options
    except FileNotFoundError:
        return "" 

#         # HTML template for the page
#         html_template = f"""
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>Select an option</title>
#         </head>
#         <body>
#             <h1>Select an option from the drop-down menu:</h1>
#             <select>
#                 {dropdown_options}
#             </select>
#         </body>
#         </html>
#         """

#         # Write the HTML code to a file or serve it using a web server
#         with open("dropdown_page.html", "w") as html_file:
#             html_file.write(html_template)

#         print("HTML page with selectable drop-down menu created successfully.")
# except Exception as error:
#     print(f"An error occurred: {error}")
