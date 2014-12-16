__author__ = 'snake'
import os


def populate():
    import xml.etree.ElementTree as ET
    tree = ET.parse('Glossary.xml')
    root = tree.getroot()

    for entry in root[0][13]:
       add_entry(entry[0].text, entry[1].text)




def add_entry(title, description):
    p = Glossary.objects.get_or_create(title=title, description=description)[0]
    return p



if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Molecular_Methods_Project.settings')
    from desktop.models import Glossary
    populate()