from django.template.response import TemplateResponse
from DiscreteRandomVariables.models import Problem
from django.http.response import HttpResponseRedirect
from DiscreteRandomVariables.DiscreteRandomVariable import getRandomVariable,\
    DiscreteRandomVariable
from DiscreteRandomVariables.Sample import Sample
from Utility.Constants import Constants
from DiscreteRandomVariables.DiscreteDistribution import PoissonDistribution, DiscreteDistribution,\
    BernoulliDistribution
from Utility.Math import Set
from DiscreteRandomVariables.forms import ProblemForm, CalculatorForm,\
    GenerateSampleForm, BivariateDistributionForm,\
    BernoulliDistributionForm, BinomialDistributionForm,\
    NegativeBinomialDistributionForm, GeometricDistributionForm,\
    HypergeometricDistributionForm, PoissonDistributionForm
from DiscreteRandomVariables.BivariateDistribution import BivariateDistribution
import random

def homepage(request):
    return TemplateResponse(request, "index.html")

def bernoulliDistribution(request):
    form = BernoulliDistributionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            random_variable = DiscreteRandomVariable(BernoulliDistribution(form.cleaned_data["probability"]))
            result = random_variable.getPossibleValue()
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "discrete_distributions/bernoulli_distribution.html", locals())

def binomialDistribution(request):
    form = BinomialDistributionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            count = form.cleaned_data["count"]
            probability = form.cleaned_data["probability"]
            sample = enumerate(Sample(DiscreteRandomVariable(BernoulliDistribution(probability)), count).result)
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "discrete_distributions/binomial_distribution.html", locals())

def negativeBinomialDistribution(request):
    form = NegativeBinomialDistributionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            probability = form.cleaned_data["probability"]
            r = form.cleaned_data["r"]
            successful = 0
            sample = []
            while successful < r:
                random_variable = DiscreteRandomVariable(BernoulliDistribution(probability))
                value = random_variable.getPossibleValue()
                if value == 1:
                    successful += 1
                sample.append(value)
            count = len(sample)
            sample = enumerate(sample)
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "discrete_distributions/negative_binomial_distribution.html", locals())

def geometricDistribution(request):
    form = GeometricDistributionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            probability = form.cleaned_data["probability"]
            sample = []
            while True:
                random_variable = DiscreteRandomVariable(BernoulliDistribution(probability))
                value = random_variable.getPossibleValue()
                sample.append(value)
                if value == 1:
                    break
            count = len(sample)
            sample = enumerate(sample)
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "discrete_distributions/geometric_distribution.html", locals())

def hypergeometricDistribution(request):
    form = HypergeometricDistributionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            total = form.cleaned_data["total"]
            defected = form.cleaned_data["defected"]
            count = form.cleaned_data["count"]
            defected_positions = enumerate(Set.randomSubset(total, defected))
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "discrete_distributions/hypergeometric_distribution.html", locals())

def poissonDistribution(request):
    form = PoissonDistributionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            error_rate = form.cleaned_data["error_rate"]
            text = form.cleaned_data["text"]
            distribution = PoissonDistribution(error_rate / 100)
            error_positions = set()
            position = 0
            while position < len(text):
                position += distribution.timeUntilNextOccurrence()
                error_positions.add(int(position))
            wrongText = ""
            for position, char in enumerate(text):
                if position in error_positions:
                    wrongText += chr(int(128 * random.random()))
                else:
                    wrongText += char
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "discrete_distributions/poisson_distribution.html", locals())

def problemList(request):
    problems = Problem.objects.all()
    return TemplateResponse(request, "problems/problem_list.html", locals())

def addProblem(request):
    form = ProblemForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/problem_list")
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "problems/add_problem.html", locals())

def viewProblem(request):
    problem = Problem.objects.get(id=request.GET["problem_id"])
    distribution = Constants.DISTRIBUTION_NAME_BY_ID[problem.distribution_id]
    return TemplateResponse(request, "problems/view_problem.html", locals())

def editProblem(request):
    problem = Problem.objects.get(id=request.GET["problem_id"])
    if request.method == "POST":
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/problem_list")
        else:
            error_message = Constants.INCORRECT_INPUT
    else:
        form = ProblemForm(instance=problem)
        problem_id = request.GET["problem_id"]
    return TemplateResponse(request, "problems/edit_problem.html", locals())

def deleteProblem(request):
    Problem.objects.get(id=request.GET["problem_id"]).delete()
    return HttpResponseRedirect("/problem_list")

def calculator(request):
    form = CalculatorForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            distribution_id = form.cleaned_data["distribution_id"]
            if distribution_id == 0:
                values = form.cleaned_data["values"].split(" ")
                probabilities = form.cleaned_data["probabilities"].split(" ")
                distribution = dict(zip(map(float, values), map(float, probabilities)))
                randomVariable = DiscreteRandomVariable(DiscreteDistribution(distribution))
            else:
                randomVariable = getRandomVariable(distribution_id,
                                                   form.cleaned_data["distribution_parameter1"],
                                                   form.cleaned_data["distribution_parameter2"],
                                                   form.cleaned_data["distribution_parameter3"])
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "random_variables/calculator.html", locals())

def generateSample(request):
    form = GenerateSampleForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            distribution_id = form.cleaned_data["distribution_id"]
            if distribution_id == 0:
                values = form.cleaned_data["values"].split(" ")
                probabilities = form.cleaned_data["probabilities"].split(" ")
                distribution = dict(zip(map(float, values), map(float, probabilities)))
                randomVariable = DiscreteRandomVariable(DiscreteDistribution(distribution))
            else:
                randomVariable = getRandomVariable(distribution_id,
                                                   form.cleaned_data["distribution_parameter1"],
                                                   form.cleaned_data["distribution_parameter2"],
                                                   form.cleaned_data["distribution_parameter3"])
            sample = Sample(randomVariable, form.cleaned_data["count"])
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "random_variables/generate_sample.html", locals())

def bivariateDistribution(request):
    form = BivariateDistributionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            values_x = form.cleaned_data["values_x"].split(" ")
            values_y = form.cleaned_data["values_y"].split("\r\n")
            rows = form.cleaned_data["probabilities"].split("\r\n")
            probabilities = []
            for row in rows:
                probabilities.append([float(value) for value in row.split(" ")])
            bivariateDistribution = BivariateDistribution(values_x, values_y, probabilities)
            independent = bivariateDistribution.independent()
        else:
            error_message = Constants.INCORRECT_INPUT
    return TemplateResponse(request, "random_variables/bivariate_distribution.html", locals())
