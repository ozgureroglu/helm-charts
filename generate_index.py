import yaml
import os

def generate_html_from_index(index_file, output_html):
    with open(index_file, 'r') as file:
        index_data = yaml.safe_load(file)

    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Helm Chart Repository</title>
        <style>
            body { font-family: Arial, sans-serif; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; }
            a { color: #007bff; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Helm Chart Repository</h1>
        <ul>
    '''

    for chart, versions in index_data.get('entries', {}).items():
        for version_info in versions:
            chart_version = version_info.get('version')
            chart_description = version_info.get('description', 'No description available')
            chart_url = version_info.get('urls', [])[0] if version_info.get('urls') else '#'

            html_content += f'<li><a href="{chart_url}">{chart} - {chart_version}</a> - {chart_description}</li>\n'

    html_content += '''
        </ul>
    </body>
    </html>
    '''

    with open(output_html, 'w') as file:
        file.write(html_content)

index_file_path = 'index.yaml' # Path to your index.yaml file
output_html_path = 'index.html' # Output HTML file path

generate_html_from_index(index_file_path, output_html_path)
