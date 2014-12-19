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
                        questionText = question.text
                        questionObject = desktop.models.Question.objects.get_or_create(topic=questionTopic, number=questionNumber,
                                                                          question=questionText, hint="")[0]
            if info.tag == "answer":
                for answer in info:
                    isCorrect = False
                    if answer.tag == "text":
                        answerText = answer.text
                        if info.attrib['fraction'] == 100:
                            isCorrect = True
                        desktop.models.Answer.objects.get_or_create(question=questionObject, answer=answerText,
                                                                    correct=isCorrect)[0]
        questionNumber += 1


if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Molecular_Methods_Project.settings')
    import desktop.models

    populate()