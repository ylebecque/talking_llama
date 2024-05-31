Qu’est-ce que LangChain ?

LangChain est un cadre open source permettant de créer des applications basées sur de grands modèles de langage (LLM). Les LLM sont de grands modèles de deep learning préentraînés sur de grandes quantités de données qui peuvent générer des réponses aux requêtes des utilisateurs (par exemple, répondre à des questions ou créer des images à partir d’invites textuelles). LangChain fournit des outils et des abstractions pour améliorer la personnalisation, la précision et la pertinence des informations générées par les modèles. Par exemple, les développeurs peuvent utiliser les composants LangChain pour créer de nouvelles chaînes d’instructions ou personnaliser des modèles existants. LangChain inclut également des composants qui permettent aux LLM d’accéder à de nouveaux jeux de données sans nécessiter un nouvel entraînement.
Pourquoi LangChain est-il important ?

Les LLM excellent pour répondre aux demandes dans un contexte général, mais rencontrent des difficultés dans un domaine spécifique pour lequel ils n’ont jamais été formés. Les invites sont des requêtes que les personnes utilisent pour obtenir des réponses auprès d’un LLM. Par exemple, un LLM peut fournir une réponse au coût d’un ordinateur en fournissant une estimation. Toutefois, il ne peut pas répertorier le prix d’un modèle d’ordinateur spécifique vendu par votre entreprise. 

Pour ce faire, les ingénieurs en machine learning doivent intégrer le LLM aux sources de données internes de l’organisation et appliquer une ingénierie de requête, une pratique dans laquelle un scientifique des données affine les entrées d’un modèle génératif avec une structure et un contexte spécifiques. 

LangChain rationalise les étapes intermédiaires pour développer de telles applications sensibles aux données, ce qui rend l’ingénierie de requête plus efficace. Il est conçu pour développer plus facilement diverses applications alimentées par des modèles de langage, notamment les chatbots, les réponses à des questions, la génération de contenu, les résumés, etc.

Les sections suivantes décrivent les avantages de LangChain.

Réutilisation des modèles de langage

Avec LangChain, les organisations peuvent réutiliser les LLM pour des applications spécifiques à un domaine sans réentraînement ni ajustement. Les équipes de développement peuvent créer des applications complexes faisant référence à des informations propriétaires afin d’améliorer les réponses des modèles. Par exemple, vous pouvez utiliser LangChain pour créer des applications qui lisent les données des documents internes stockés et les synthétisent en réponses conversationnelles. Vous pouvez créer un flux de travail RAG (Retrieval Augmented Generation) qui introduit de nouvelles informations dans le modèle de langage lors de l’invite. La mise en œuvre de flux de travail sensibles au contexte tels que RAG réduit les hallucinations du modèle et améliore la précision des réponses. 

Simplification du développement en IA

LangChain simplifie le développement en intelligence artificielle (IA) en supprimant la complexité des intégrations de sources de données et en les affinant rapidement. Les développeurs peuvent personnaliser les séquences pour créer rapidement des applications complexes. Au lieu de programmer la logique métier, les équipes logicielles peuvent modifier les modèles et les bibliothèques fournis par LangChain afin de réduire le temps de développement. 

Aide aux développeurs

LangChain fournit aux développeurs d’IA des outils pour connecter les modèles de langage à des sources de données externes. Il est open source et soutenu par une communauté active. Les organisations peuvent utiliser LangChain gratuitement et bénéficier de l’assistance d’autres développeurs maîtrisant le cadre.
Comment fonctionne LangChain ?

Avec LangChain, les développeurs peuvent adapter un modèle de langage de manière flexible à des contextes métier spécifiques en désignant les étapes nécessaires pour produire le résultat souhaité. 

Chaînes

Les chaînes sont le principe fondamental qui sous-tend les divers composants de l’IA dans LangChain pour fournir des réponses sensibles au contexte. Une chaîne est une série d’actions automatisées allant de la requête de l’utilisateur à la sortie du modèle. Par exemple, les développeurs peuvent utiliser une chaîne pour :

La connexion à différentes sources de données
La génération de contenu unique
La traduction de plusieurs langues
La réponse aux questions des utilisateurs 
Liens

Les chaînes sont faites de liens. Chaque action que les développeurs enchaînent pour former une séquence enchaînée est appelée lien. Grâce aux liens, les développeurs peuvent diviser les tâches complexes en plusieurs tâches plus petites. Voici des exemples de liens :

Formatage des données saisies par l’utilisateur 
Envoi d’une requête à un LLM 
Extraction de données depuis le stockage dans le cloud
Traduction d’une langue à l’autre
Dans le cadre LangChain, un lien accepte les entrées de l’utilisateur et les transmet aux bibliothèques LangChain pour traitement. LangChain permet également de réorganiser les liens pour créer différents flux de travail d’IA. 

Présentation

Pour utiliser LangChain, les développeurs installent le cadre en Python à l’aide de la commande suivante :

pip install langchain

Les développeurs utilisent ensuite les blocs de construction de chaînes ou le LangChain Expression Language (LCEL) pour composer des chaînes à l’aide de commandes de programmation simples. La fonction chain() transmet les arguments d’un lien aux bibliothèques. La commande execute() récupère les résultats. Les développeurs peuvent transmettre le résultat du lien actuel au lien suivant ou le renvoyer comme résultat final. 

Vous trouverez ci-dessous un exemple de fonction de chaîne de chatbot qui renvoie les détails du produit dans plusieurs langues.

chain([
retrieve_data_from_product_database().
send_data_to_language_model().
   format_output_in_a_list().
  translate_output_in_target_language()
])

Quels sont les principaux composants de LangChain ?

À l’aide de LangChain, les équipes logicielles peuvent créer des systèmes de modèles de langage sensibles au contexte avec les modules suivants. 

Interface LLM

LangChain fournit des API avec lesquelles les développeurs peuvent se connecter et interroger des LLM à partir de leur code. Les développeurs peuvent interagir avec des modèles publics et propriétaires tels que GPT, Bard et PaLM avec LangChain en effectuant de simples appels d’API au lieu d’écrire du code complexe.

Modèles d’invite

Les modèles d’invite sont des structures prédéfinies que les développeurs utilisent pour formater de manière cohérente et précise les requêtes pour les modèles d’IA. Les développeurs peuvent créer un modèle d’invite pour les applications de chatbot, quelques étapes d’apprentissage ou fournir des instructions spécifiques aux modèles de langage. De plus, ils peuvent réutiliser les modèles dans plusieurs applications et modèles de langage. 

Agents

Les développeurs utilisent les outils et les bibliothèques fournis par LangChain pour composer et personnaliser des chaînes existantes pour des applications complexes. Un agent est une chaîne spéciale qui invite le modèle de langage à choisir la meilleure séquence en réponse à une requête. Lorsqu’ils utilisent un agent, les développeurs fournissent les informations de l’utilisateur, les outils disponibles et les étapes intermédiaires possibles pour atteindre les résultats souhaités. Le modèle de langage renvoie ensuite une séquence viable d’actions que l’application peut effectuer.  

Modules de récupération

LangChain permet l’architecture de systèmes RAG avec de nombreux outils pour transformer, stocker, rechercher et récupérer des informations qui affinent les réponses des modèles de langage. Les développeurs peuvent créer des représentations sémantiques d’informations à l’aide d’intégrations de mots et les stocker dans des bases de données vectorielles locales ou dans le cloud. 

Mémoire

Certaines applications de modèles de langage conversationnel affinent leurs réponses à l’aide d’informations rappelées lors d’interactions passées. LangChain permet aux développeurs d’inclure des capacités de mémoire dans leurs systèmes. Il prend en charge :

Des systèmes de mémoire simples qui mémorisent les conversations les plus récentes. 
Des structures de mémoire complexes qui analysent les messages historiques pour renvoyer les résultats les plus pertinents. 
Rappels

Les rappels sont des codes que les développeurs placent dans leurs applications pour enregistrer, surveiller et diffuser des événements spécifiques dans les opérations LangChain. Par exemple, les développeurs peuvent suivre le moment où une chaîne a été appelée pour la première fois et les erreurs rencontrées lors des rappels. 
