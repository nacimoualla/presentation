from pptx import Presentation
from pptx.util import Inches

prs = Presentation()

# Title Slide
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Multi-Threading & Synchronisation"
subtitle.text = "Maîtriser l'exécution parallèle et éviter le chaos.\n\nPrésenté par :\n👤 Nacim Oualla\n👤 Essaqy Douae\n👤 Yassmine Mouden\n👤 Ouachikh Zakaria"

# Bullet slide layout
bullet_slide_layout = prs.slide_layouts[1]

def add_bullet_slide(title_text, bullet_points):
    slide = prs.slides.add_slide(bullet_slide_layout)
    shapes = slide.shapes
    title_shape = shapes.title
    body_shape = shapes.placeholders[1]
    title_shape.text = title_text
    tf = body_shape.text_frame
    tf.text = bullet_points[0]
    for pt in bullet_points[1:]:
        p = tf.add_paragraph()
        p.text = pt
    return slide

add_bullet_slide("Qu'est-ce qu'un Thread ?", [
    "Un processus est une application en cours d'exécution.",
    "Un thread est la plus petite unité de traitement.",
    "Attention : Les threads partagent le même espace mémoire !"
])

add_bullet_slide("Pourquoi le Multi-Threading ?", [
    "1. Réactivité ⚡: L'interface utilisateur ne gèle pas pendant les longs calculs en arrière-plan.",
    "2. Performance 🚀: Exploitation maximale et simultanée des processeurs multi-cœurs modernes.",
    "3. Économie 💾: Créer un thread coûte beaucoup moins de mémoire que de créer un nouveau processus."
])

add_bullet_slide("Le Danger : Race Conditions", [
    "Que se passe-t-il si deux threads modifient la même donnée en même temps ?",
    "-> Données corrompues",
    "-> Comportements imprévisibles",
    "-> Crash de l'application"
])

add_bullet_slide("La Synchronisation 🛡️", [
    "Mettre de l'ordre dans l'exécution avec des verrous.",
    "Mutex : Verrou d'exclusion mutuelle. Un seul thread à la fois.",
    "Sémaphore : Limitation d'accès. N threads maximum autorisés.",
    "Moniteur : Approche Objet. Méthodes synchronisées nativement."
])

add_bullet_slide("Le Cauchemar : Deadlocks", [
    "L'Interblocage fatal.",
    "\"Le Thread A attend que le Thread B lâche une ressource... mais le Thread B attend que le Thread A lâche la sienne.\"",
    "Résultat : Tout se fige. 🛑"
])

# Processus vs Thread table
slide = prs.slides.add_slide(prs.slide_layouts[5]) # Title only
slide.shapes.title.text = "Processus vs Thread"
rows = 5
cols = 2
left = Inches(1.0)
top = Inches(2.0)
width = Inches(8.0)
height = Inches(3.0)
table = slide.shapes.add_table(rows, cols, left, top, width, height).table

# Set headers
table.cell(0, 0).text = "Processus"
table.cell(0, 1).text = "Thread"

# Add data
data = [
    ("Espaces mémoire isolés", "Mémoire partagée"),
    ("Lourd (Temps CPU)", "Léger et rapide"),
    ("Isolation (si l'un plante, l'autre survit)", "Faible isolation (un crash tue le processus)"),
    ("Communication (IPC) lente", "Communication très rapide")
]

for row_idx, row_data in enumerate(data):
    for col_idx, text in enumerate(row_data):
        table.cell(row_idx + 1, col_idx).text = text

add_bullet_slide("Langages & Concurrence", [
    "Python : Le GIL limite à un seul thread actif à la fois (pas de vrai parallélisme CPU natif pour les threads).",
    "Java / C++ : Threads OS natifs. Outils avancés (Pools, Futures). Très performants mais complexes.",
    "Go / Node.js : Goroutines (Go) : ultra-légers. Event-loop (Node) : asynchronisme mono-thread."
])

add_bullet_slide("Bonnes Pratiques ✅", [
    "Minimiser les données partagées entre les threads.",
    "Garder les sections critiques (verrouillées) très courtes.",
    "Toujours utiliser unlock() dans un bloc finally."
])

# Closing slide
slide = prs.slides.add_slide(title_slide_layout)
slide.shapes.title.text = "Merci !"
slide.placeholders[1].text = "Avez-vous des questions ?"

prs.save("presentation.pptx")
print("PowerPoint presentation generated successfully!")
