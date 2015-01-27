import os


def populate():

    desktop.models.Video.objects.get_or_create(title="Introduction", link="http://youtu.be/GgcGFyDvyFA", topic="General")[0]

    desktop.models.Video.objects.get_or_create(title="PCR Primer Design", link="http://youtu.be/c-f1H07D_70", topic="Primers")[0]

    desktop.models.Video.objects.get_or_create(title="Restriction Mapping Part 1", link="http://youtu.be/yR_heZ4n4Gc", topic="Restriction Mapping")[0]

    desktop.models.Video.objects.get_or_create(title="Restriction Mapping Part 2", link="http://youtu.be/MeTWD8ECeiQ", topic="Restriction Mapping")[0]


if __name__ == '__main__':

    import desktop.models

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Molecular_Methods_Project.settings')

    populate()