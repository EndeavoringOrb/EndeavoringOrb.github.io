import os
import yaml
import markdown
import re
from markupsafe import Markup
from jinja2 import Environment, FileSystemLoader
import json
import shutil


def process_content(content, project_dir):
    """Process markdown content similar to the Flask app."""
    # Regex to find {% include <filename> %} tags
    include_pattern = re.compile(r'{%\s*include\s+([^\s]+)\s*%}')

    def handle_include(match):
        filename = match.group(1)
        include_path = os.path.join(project_dir, filename)
        # Check if the file exists
        if os.path.exists(include_path):
            with open(include_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            return file_content
        else:
            return f'<!-- File {filename} not found -->'

    # Replace {% include filename %} tags with file content
    content = re.sub(include_pattern, handle_include, content)

    # Convert markdown to HTML
    html_content = Markup(
        markdown.markdown(content, extensions=['extra', 'codehilite', 'toc'])
    )

    return html_content


def generate_site():
    """Generate the static site."""
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))

    # Generate index.html
    with open('profile.json', 'r', encoding='utf-8') as f:
        profile_data = json.load(f)
    template = env.get_template('index.html')
    html = template.render(profile=profile_data)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Generated index.html')

    # Generate project pages
    projects_dir = 'projects'
    output_dir = 'projects_html'
    if os.path.exists(projects_dir):
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        for project_name in os.listdir(projects_dir):
            project_dir = os.path.join(projects_dir, project_name)
            if os.path.isdir(project_dir):
                generate_project_html(env, project_dir, project_name, output_dir)


def generate_project_html(env, project_dir, project_name, output_dir):
    """Generate HTML for a specific project."""
    # Load project metadata
    metadata_path = os.path.join(project_dir, 'metadata.yaml')
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r') as f:
            metadata = yaml.safe_load(f)
    else:
        metadata = {'title': project_name.capitalize(), 'sections': []}

    # Load project content
    content_path = os.path.join(project_dir, 'content.md')
    if os.path.exists(content_path):
        with open(content_path, 'r', encoding='utf-8') as f:
            content = f.read()
        html_content = process_content(content, project_dir)
    else:
        html_content = Markup('<p>No content available for this project.</p>')

    # Render the project template
    template = env.get_template('project.html')
    html = template.render(
        metadata=metadata,
        content=html_content,
        project_name=project_name
    )

    # Create projects directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write the final HTML file
    with open(f'{output_dir}/{project_name}.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Generated {output_dir}/{project_name}.html')


def main():
    """Main function to generate all static files."""
    generate_site()
    print('Static site generation complete!')


if __name__ == '__main__':
    main()