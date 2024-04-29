from django.contrib import admin
from .models import *
from django.conf import settings
from django.core.files.storage import default_storage
from _ast import Attribute
from django.shortcuts import get_object_or_404
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission




# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(AnneeUniv)
admin.site.register(Matiere)
admin.site.register(UE)
admin.site.register(Formation)
admin.site.register(Programme)
admin.site.register(Specialite)
#admin.site.register(Option)
admin.site.register(Enseignant)
admin.site.register(Charge)
admin.site.register(Module)
admin.site.register(Activite)
admin.site.register(Groupe)
admin.site.register(Section)
admin.site.register(Seance)
admin.site.register(AbsenceEtudiant)
admin.site.register(AbsenceEnseignant)
admin.site.register(Diplome)
admin.site.register(ModulesSuivis)
admin.site.register(Etudiant)
admin.site.register(Inscription)
admin.site.register(Periode)
admin.site.register(Note)
admin.site.register(Evaluation)
admin.site.register(Resultat)
admin.site.register(Reponse)
admin.site.register(Question)
admin.site.register(Feedback)
admin.site.register(DomaineConnaissance)
admin.site.register(PeriodeProgramme)
admin.site.register(CompetenceFamily)
admin.site.register(Competence)
admin.site.register(CompetenceElement)
admin.site.register(MatiereCompetenceElement)
admin.site.register(Organisme)
admin.site.register(Wilaya)
admin.site.register(Personnel)
admin.site.register(ResidenceUniv)
admin.site.register(GoogleCalendar)
admin.site.register(Salle)
admin.site.register(PFE)
admin.site.register(Soutenance)
admin.site.register(Equipe)
admin.site.register(CompetenceEvalConfig)
admin.site.register(Permission)
admin.site.register(Doctorant)
admin.site.register(These)
admin.site.register(Projet)
admin.site.register(Autorite)
admin.site.register(DocumentConfig)
admin.site.register(Cycle)
admin.site.register(EtatAvancement)
admin.site.register(Critere)
admin.site.register(OptionCritere)
admin.site.register(SeminaireSuivi)
admin.site.register(PV)
admin.site.register(EnregistrementEtudiant)
admin.site.register(Preinscription)
admin.site.register(Offre)
admin.site.register(Candidature)
admin.site.register(InscriptionPeriode)

# stage register
admin.site.register(EDTStartChoices)
admin.site.register(ActivationInfo)
admin.site.register(Examen)

