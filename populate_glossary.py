import os
import xml.etree.ElementTree


def populate():

    tree = xml.etree.ElementTree.parse('Glossary.xml')

    root = tree.getroot()

    for entry in root[0][13]:
        desktop.models.Glossary.objects.get_or_create(title=entry[0].text, description=entry[1].text)[0]


if __name__ == '__main__':

    import desktop.models

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Molecular_Methods_Project.settings')

    populate()