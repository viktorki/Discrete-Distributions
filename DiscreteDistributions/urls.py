from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns("",

    url(r"^admin/", include(admin.site.urls)),
    
    #Homepage
    url(r"^$", "DiscreteRandomVariables.views.homepage"),
    
    #Problems
    url(r"^problem_list/", "DiscreteRandomVariables.views.problemList"),
    url(r"^add_problem/", "DiscreteRandomVariables.views.addProblem"),
    url(r"^view_problem/", "DiscreteRandomVariables.views.viewProblem"),
    url(r"^edit_problem/", "DiscreteRandomVariables.views.editProblem"),
    url(r"^delete_problem/", "DiscreteRandomVariables.views.deleteProblem"),
    
    #Random variables
    url(r"^calculator/", "DiscreteRandomVariables.views.calculator"),
    url(r"^generate_sample/", "DiscreteRandomVariables.views.generateSample"),
    url(r"^bivariate_distribution/", "DiscreteRandomVariables.views.bivariateDistribution"),
    
    #Discrete Distributions
    url(r"^bernoulli_distribution/", "DiscreteRandomVariables.views.bernoulliDistribution"),
    url(r"^binomial_distribution/", "DiscreteRandomVariables.views.binomialDistribution"),
    url(r"^negative_binomial_distribution/", "DiscreteRandomVariables.views.negativeBinomialDistribution"),
    url(r"^geometric_distribution/", "DiscreteRandomVariables.views.geometricDistribution"),
    url(r"^hypergeometric_distribution/", "DiscreteRandomVariables.views.hypergeometricDistribution"),
    url(r"^poisson_distribution", "DiscreteRandomVariables.views.poissonDistribution")
)
