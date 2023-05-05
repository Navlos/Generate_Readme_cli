import argparse
import markdown

def generate_readme(project_name,description,installation,usage,contribution):
    readme_template = """
    
    ## project_name
    {project_name}
    
    ## description
    {description}
    
    ## Installation
    {installation}
    
    ## Usage
    {usage}
    
    ## Contibuting
    {contributing}
    
    """
    
    readme_content = readme_template.format(project_name = project_name)
    
    