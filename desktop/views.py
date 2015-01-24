import os
import urllib
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from desktop.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from desktop.models import Glossary
from desktop.models import QQuestion, Answer, MQuestion
import json as simplejson
#Django Q Objects to handle queries
from django.db.models import Q

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('index.html', context_dict, context)

@login_required
def revision(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('revision.html', context_dict, context)


@login_required
def labs(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('labs.html', context_dict, context)

@login_required
def pcrlab(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('pcrlab.html', context_dict, context)

@login_required
def pcrlabpdf(request):
    context=RequestContext(request)
    context_dict={}
    return render_to_response('pcrlabpdf.html', context_dict, context)


@login_required
def ligation(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('ligation.html',context_dict,context)

@login_required
def bwscreening(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('bwscreening.html',context_dict,context)

@login_required
def plasmid(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('plasmid.html',context_dict,context)

@login_required
def dna(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('dna.html', context_dict, context)

@login_required
def quantpcr(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('quantpcr.html', context_dict, context)


@login_required
def primersquizzes(request):
    context= RequestContext(request)

    context_dict={}

    context_dict['questions'] = QQuestion.objects.all() #filter(topic=2)
    context_dict['answers'] = Answer.objects.all()#filter(question__topic=2)
    return render_to_response('primersquizzes.html',context_dict,context)


@login_required
def checkAnswer(request):
    answers = Answer.objects.filter()
    questions = QQuestion.objects.filter()

    checked_boxes = request.POST.getlist('ans[]')
    corr_ans = []
    user_ans = []

  #if len(answers) == len(checked_boxes):
   # feedback.append("A wise guy, eh?")
  #else:
    i=0
    while i<len(questions):
        for answer in answers:
            if (answer.question==questions[i]):
                if(answer.correct==True):
                    corr_ans.append(str(answer.answer))
                    user_ans.append(str(checked_boxes[i]))


        i=i+1

    data = zip(questions,corr_ans,user_ans)
    context = {'data': data}
    return render(request, 'correct.html', context)


@login_required
def glossary(request):

    context = RequestContext(request)

    context_list = Glossary.objects.order_by('title')
    context_dict={}

    #Created a structure for each letter and then pass it into context_dictionary
    context_dict['terms1'] = context_list.exclude(title__regex=r'^[a-zA-Z]')
    context_dict['termsA'] = context_list.filter(Q(title__istartswith='A'))
    context_dict['termsB'] = context_list.filter(Q(title__istartswith='B'))
    context_dict['termsC'] = context_list.filter(Q(title__istartswith='C'))
    context_dict['termsD'] = context_list.filter(Q(title__istartswith='D'))
    context_dict['termsE'] = context_list.filter(Q(title__istartswith='E'))
    context_dict['termsF'] = context_list.filter(Q(title__istartswith='F'))
    context_dict['termsG'] = context_list.filter(Q(title__istartswith='G'))
    context_dict['termsH'] = context_list.filter(Q(title__istartswith='H'))
    context_dict['termsI'] = context_list.filter(Q(title__istartswith='I'))
    context_dict['termsJ'] = context_list.filter(Q(title__istartswith='J'))
    context_dict['termsK'] = context_list.filter(Q(title__istartswith='K'))
    context_dict['termsL'] = context_list.filter(Q(title__istartswith='L'))
    context_dict['termsM'] = context_list.filter(Q(title__istartswith='M'))
    context_dict['termsN'] = context_list.filter(Q(title__istartswith='N'))
    context_dict['termsO'] = context_list.filter(Q(title__istartswith='O'))
    context_dict['termsP'] = context_list.filter(Q(title__istartswith='P'))
    context_dict['termsQ'] = context_list.filter(Q(title__istartswith='Q'))
    context_dict['termsR'] = context_list.filter(Q(title__istartswith='R'))
    context_dict['termsS'] = context_list.filter(Q(title__istartswith='S'))
    context_dict['termsT'] = context_list.filter(Q(title__istartswith='T'))
    context_dict['termsU'] = context_list.filter(Q(title__istartswith='U'))
    context_dict['termsV'] = context_list.filter(Q(title__istartswith='V'))
    context_dict['termsW'] = context_list.filter(Q(title__istartswith='W'))
    context_dict['termsX'] = context_list.filter(Q(title__istartswith='X'))
    context_dict['termsY'] = context_list.filter(Q(title__istartswith='Y'))
    context_dict['termsZ'] = context_list.filter(Q(title__istartswith='Z'))

    return render_to_response('glossary.html', context_dict, context)

@login_required
def videos(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('videos.html',context_dict,context)


@login_required
def project(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('project.html',context_dict,context)

@login_required
def revision(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('revision.html',context_dict,context)

@login_required
def converterconcentration(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('converterconcentration.html',context_dict,context)

@login_required
def converterdilutions(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('converterdilutions.html',context_dict,context)

@login_required
def convertermass(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('convertermass.html',context_dict,context)

@login_required
def convertermolarity(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('convertermolarity.html',context_dict,context)

@login_required
def convertervolume(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('convertervolume.html',context_dict,context)


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors,

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
        'register.html',
        {'user_form': user_form, 'registered': registered},
        context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/desktop/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/desktop/')


@login_required
def mapping(request, question_num):
    context = RequestContext(request)
    questionList = MQuestion.objects.order_by('Number')[:]
    currQues = MQuestion.objects.get(Number = question_num)

    e1 = currQues.Enzyme1.split(":")
    e2 = currQues.Enzyme2.split(":")
    e3 = currQues.Enzyme3.split(":")

    ques = "Uncut plasmid (circular) " + str(float(currQues.Size) / 10) + "kb \n"

    ques = ques + e1[0] + "  "
    for i in xrange(1,len(e1)):
        ques = ques + " " + str(float(e1[i]) / 10) + ","
    ques = ques[:-1] + " kb\n"

    ques = ques + e2[0] + "  "
    for i in xrange(1,len(e2)):
        ques = ques + " " + str(float(e2[i]) / 10) + ","
    ques = ques[:-1] + " kb\n"

    ques = ques + e3[0] + "  "
    for i in xrange(1,len(e3)):
        ques = ques + " " + str(float(e3[i]) / 10) + ","
    ques = ques[:-1] + " kb\n"

    ans = currQues.Answer
    ans = ans.split(":")
    ans1 = simplejson.dumps(ans[0].split(","))
    ans2 = simplejson.dumps(ans[1].split(","))
    ans3 = simplejson.dumps(ans[2].split(","))
    context_dict = {'size':currQues.Size, 'firstMap': ans1, 'secondMap': ans2, 'finalMap': ans3, 'question':ques, 'questions':questionList, 'number':int(question_num)}
    return render_to_response('mapping.html', context_dict, context)


@login_required
def pdf(request, filename):
    fullpath = os.path.join(PDF_PATH, filename)
    response = HttpResponse(file(fullpath).read())
    response['Content-Type'] = 'application/pdf'
    response['Content-disposition'] = 'attachment'
    return response
