import argparse
import markdown


def generate_readme(project_name, description, installation, usage, contribution, contact):
    readme_template = """
# {project_name}

{description}

## Installation

{installation}

## Usage

{usage}

## Contributing

{contribution}

## Contact

{contact}
"""
    readme_content = readme_template.format(
        project_name=project_name,
        description=description,
        installation=installation,
        usage=usage,
        contribution=contribution,
        contact=contact
    )
    return markdown.markdown(readme_content)

    readme_content = readme_template.format(
        project_name=project_name, description=description, installation=installation, usage=usage, contribution=contribution)

    return markdown.markdown(readme_content)


# command line interface
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a README file for a project')
    parser.add_argument('--project-name', required=True,
                        help='The name of the project')
    parser.add_argument('--description', required=True,
                        help='A brief description of the project')
    parser.add_argument('--installation', required=True,
                        help='Installation instructions for the project')
    parser.add_argument('--usage', required=True,
                        help='Usage examples for the project')
    parser.add_argument('--contribution', required=True,
                        help='Contribution guidelines for the project')
    parser.add_argument('--contact', required=True,
                        help='Contact information for the project owner')
    args = parser.parse_args()

    # Generate the README file
    readme_content = generate_readme(
        project_name=args.project_name,
        description=args.description,
        installation=args.installation,
        usage=args.usage,
        contribution=args.contribution,
        contact=args.contact
    )

    # Print the Markdown-formatted README to the console
    # print(readme_text)
    
    # put the generated readme in a README.MD FILE
    
def write_to_file(readme_content):
    print('testing')
    # open README.MD file in write mode
    with open('README.md', "w") as f:
        # write the generate content to the fuke
        f.write(readme_content)
    print('README file successfully generated as README.md ')

write_to_file(readme_content)