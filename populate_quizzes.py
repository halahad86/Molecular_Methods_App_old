import os


def populate():
    import xml.etree.ElementTree as ET

    tree = ET.parse('General.xml')
    root = tree.getroot()

    questionTopic = "General"
    questionNumber = 0
    answerArray = []

    for question in root:
        for info in question:
            if info.tag == "questiontext":
                for question in info:
                    if question.tag == "text":
                        print "Q: ", question.text
                        questionText = question.text
                        ##question = desktop.models.Question.objects.get_or_create(title=title, description=description)[
                            ##0]
            if info.tag == "answer":
                for answer in info:
                    if answer.tag == "text":
                        print "A: ", answer.text
                        #desktop.models.Answer.objects.get_or_create(title=title, description=description)[0]
        questionNumber += 1


if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Molecular_Methods_Project.settings')
    import desktop.models

    populate()