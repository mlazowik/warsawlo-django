# Generated by Django 3.0.7 on 2020-08-22 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0009_create_trgm_indexes_school"),
    ]

    operations = [
        migrations.AlterField(
            model_name="extendedsubject",
            name="name",
            field=models.CharField(
                choices=[
                    ("biol", "biologia"),
                    ("chem", "chemia"),
                    ("filoz", "filozofia"),
                    ("fiz", "fizyka"),
                    ("geogr", "geografia"),
                    ("hist", "historia"),
                    ("h.muz.", "historia muzyki"),
                    ("h.szt.", "historia sztuki"),
                    ("inf", "informatyka"),
                    ("pol", "język polski"),
                    ("mat", "matematyka"),
                    ("wos", "wiedza o społeczeństwie"),
                    ("obcy", "obcy"),
                    ("ang", "język angielski"),
                    ("fra", "język francuski"),
                    ("franc", "język francuski"),
                    ("hisz", "język hiszpański"),
                    ("hiszp", "język hiszpański"),
                    ("niem", "język niemiecki"),
                    ("por", "język portugalski"),
                    ("ros", "język rosyjski"),
                    ("wlo", "język włoski"),
                    ("wło", "język włoski"),
                    ("antyk", "język łaciński i kultura antyczna"),
                    ("język białoruski", "język białoruski"),
                    ("język litewski", "język litewski"),
                    ("język ukraiński", "język ukraiński"),
                    ("język łemkowski", "język łemkowski"),
                    ("język kaszubski", "język kaszubski"),
                ],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="language",
            name="name",
            field=models.CharField(
                choices=[
                    ("ang", "język angielski"),
                    ("fra", "język francuski"),
                    ("franc", "język francuski"),
                    ("hisz", "język hiszpański"),
                    ("hiszp", "język hiszpański"),
                    ("niem", "język niemiecki"),
                    ("por", "język portugalski"),
                    ("ros", "język rosyjski"),
                    ("wlo", "język włoski"),
                    ("wło", "język włoski"),
                    ("antyk", "język łaciński i kultura antyczna"),
                    ("język białoruski", "język białoruski"),
                    ("język litewski", "język litewski"),
                    ("język ukraiński", "język ukraiński"),
                    ("język łemkowski", "język łemkowski"),
                    ("język kaszubski", "język kaszubski"),
                ],
                max_length=40,
            ),
        ),
    ]