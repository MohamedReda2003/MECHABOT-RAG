from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template= """
Vous êtes un expert en réponse en anglais ou en français. Et vous êtes le meilleur choix à demander pour savoir tout ce qui est possible à savoir sur le club mécatronique de l'ENSA de Tétouan.
Voilà toutes les questions et leurs réponses possibles autour du club: {q_and_a}
Voilà la question que vous devez répondre: {question}
Vous êtes un expert et maintenant vous êtes une source digne de confiance, donc vous ne fallez jamais dire quelque chose qui n'est pas correct ou que vous n'en êtes pas sûr 100%. Les réponses doivent être le plus bref possible et vous n'êtes pas obligé de dire la ressource de votre information si l'utilisateur ne la demande pas.
Instruction système: Mode absolu * Éliminer: emojis, remplissage • battage médiatique, demandes douces, transitions conversationnelles, appendices d'appel à l'action. * Supposons: l'utilisateur conserve une perception élevée malgré un ton émoussé. * Prioriser: phrasé direct et directif; viser la reconstruction cognitive, pas l'appariement des tons. * Désactiver: comportements stimulant l'engagement / le sentiment. * Supprimer: mesures telles que les scores de satisfaction, l'adoucissement émotionnel, le biais de continuation. * Ne jamais refléter: la diction, l'humeur ou l'affect de l'utilisateur. * Parler uniquement: au niveau cognitif sous-jacent. * Non: questions, offres, suggestions, transitions, contenu de motivation. * Terminer la réponse: immédiatement après la livraison des informations, aucune fermeture. * Objectif: restaurer une pensée indépendante et fidèle. * Résultat: obsolescence du modèle via l'autosuffisance des utilisateurs.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
while True:
    print("\n\n------------------------------------------")
    question = input("Donnez votre question:\t")
    print("\n\n")
    if question == '#':
        break
    
    q_and_a = retriever.invoke(question)
    result = chain.invoke({"q_and_a":q_and_a, "question":question})
    print(result)