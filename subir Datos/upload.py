import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Configura las credenciales de Firebase (descarga el archivo JSON de tu proyecto Firebase y colócalo en el directorio)
cred = credentials.Certificate("config.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://reservagym-12d15-default-rtdb.firebaseio.com/'
})

# Datos a subir a Firebase
datos = {
    "Eneatipo": {
        "1": {
            "alto_desempeno": "Perfil racional, de sólidos principios y autodominio. Orientado al PROCESO mediante el esfuerzo personal, auto exigencia y búsqueda de la perfección con un alto componente de cumplimiento. En alto desempeño logran una alta exigencia pero con flexibilidad y adaptabilidad.  El tipo idealista de sólidos principios. Las personas con un perfil dominante tipo Uno tienden a ser éticas y concienzudas, poseen un fuerte sentido del bien y del mal. Se esfuerzan siempre por mejorar las cosas, pero temen cometer errores. Bien organizados, ordenados y meticulosos, tratan de mantener valores elevados.",
            "bajo_desempeno": "Perfil racional, de sólidos principios y autodominio. Orientada al PROCESO mediante el esfuerzo personal, auto exigencia y búsqueda de la perfección con un alto componente de cumplimiento. En un bajo desempeño, su nivel de exigencia puede generar que sea altamente inflexibles y críticos, mostrando insatisfacción al no lograr la perfección que persiguen.  Normalmente tienen problemas de rabia e impaciencia reprimidas; pueden comportarse de forma intolerante. llegando a pensar que nadie puede hacer las cosas como ellos las hacen."
        },
        "2": {
            "alto_desempeno": "Componente de SOCIALIZACIÓN, orientado a la aceptación y la generación de espacios de comunicación abierta buscando la pertenencia. El tipo preocupado, orientado a los demás; los Dos son comprensivos, sinceros y bondadosos; son amistosos, generosos y abnegados.En su mejor aspecto, el Dos sano es generoso, altruista y siente un amor incondicional por sí mismo y por los demás; tienen gran capacidad de servicio, son colaboradores y muy buenos coequiperos.",
            "bajo_desempeno": "Componente de SOCIALIZACIÓN, orientado a la aceptación y la generación de espacios de comunicación abierta buscando la pertenencia. En un bajo desempeño tienen problemas para cuidar de sí mismos y reconocer sus propias necesidades, desean intimar con los demás y suelen hacer cosas por ellos para sentirse necesitados. Pueden ser sentimentales, aduladores y obsequiosos."
        },
        "3": {
            "alto_desempeno": "Energía de tipo emocional con un claro enfoque al LOGRO y los resultados, con necesidad de reconocimiento y alta eficiencia. El tipo adaptable y orientado al éxito. Las personas tipo Tres son seguras de sí mismas, atractivas y encantadoras; ambiciosas, competentes y enérgicas, también pueden ser muy conscientes de su posición y estar muy motivadas por el progreso personal. Suelen preocuparse por su imagen y por lo que los demás piensan de ellas.",
            "bajo_desempeno": "Energía de tipo emocional con un claro enfoque al LOGRO y los resultados, con necesidad de reconocimiento y alta eficiencia. Su peor temor es el fracaso, por lo cual ante una sensación de esto, pueden buscar brillar solos, obtener los resultados de una forma bastante ambiciosa e individualista, centrándose en sus necesidades. Normalmente tienen problemas de adicción al trabajo y de competitividad, desean lograr resultados en función de ser reconocidos y sentirse valorados. Tienden a ser exagerados en su apariencia, con ella buscan ser centro de atracción." 
        },
        "4": {
            "alto_desempeno": "Energía orientada a la INTERIORIZACIÓN en donde lo más importante es la satisfacción de las necesidades de tipo individual en función de la autenticidad. En alto desempeño tienden a ser centrados, auténticos y muy sinceros; su gran origionalidad puede hacerle ser recursivo, altamente inspirador, quien promueve ideas creativas e innovadoras para encontrar formas difrentes a las convencionales. Con gran capacidad de conectar con sus emociones, lo cual lo lleva a usar estas en sus procesos creativos. " ,
            "bajo_desempeno": "Energía orientada a la INTERIORIZACIÓN en donde lo más importante es la satisfacción de las necesidades de tipo individual en función de la autenticidad. En un bajo desempeño, puede conectar con sus emociones de una forma un tanto exagerada y tener humor cambiante. Su miedo mas grande es ser uno mas y perder su originalidad. En este estado puede ser melodramático, apartado, no aceptar normas o estructuras donde sienta que está siendo encajado o parametrizado como los demás." 
        },
        "5": {
            "alto_desempeno": "Energía intelectual orientada a la INTERIORIZACIÓN mediante la comprensión profunda de los eventos del entorno y su asimilación a la realidad. Este perfil tiende a especializarse en temas, en alto desempeño pueden ser un experto, conocedor con un alto nivel de profundidad en sus diálogos, por lo cual suelen ser buscados como consejeros. Son personas que se comportan de forma interesante, centrados, abiertos a los demás. siendo reconocidos por su conocimiento, fundamentación de sus diálogos y un alto dominio emocional." ,
            "bajo_desempeno": "Energía intelectual orientada a la INTERIORIZACIÓN mediante la comprensión profunda de los eventos del entorno y su asimilación a la realidad. En bajo desempeño, tienden a ser personas aisladas del entorno externo, quienes se refugian en el conocimiento y su mundo interno, generando barreras con el exterior. El temor mas grande de este eneatipo es a la ignorancia, por lo cual se aferra al conocimiento y a la experticie como una forma de mostrar valía. En bajo desempeño pueden ser aislados, arrogantes y egoístas por su conocimiento, apáticos, de carácter fuerte y con tendencia a ser solitarios." 
        },
        "6": {
            "alto_desempeno": "Componente de CUMPLIMIENTO, con un esquema de previsión y anticipación, lleva a la planeación bajo el concepto de visión a mediano y largo plazo. Son personas comprometidas, cumplidoras, quines actúan de forma colaborativa y servicial, siemprede forma precavida y enfocada. En alto desempeño, tienen una gran capacidad al servicio, son personas comprometidas, familiares, y altamente leales, quienes se alinean a su grupo y permiten transmitir su capacidad de planeación y contemplar diferentes opciones y escenarios. " ,
            "bajo_desempeno": "Componente de CUMPLIMIENTO, con un esquema de previsión y anticipación, lleva a la planeación bajo el concepto de visión a mediano y largo plazo. Este perfil puede llegar a un bajo desempeño por una situación que genere sensación de amenaza, donde sienta en riesgo su seguridad, lo cual limita su capacidad de actuar, pudiendo frenarse y frenar a otros a la acción o buscando alta validación para accionar o tomar decisiones. En escenarios de tensión, puede ser exagerado, visualizando el peor escenario, pudiendo comportarse de forma pesimista, angustiado, temerosa o hasta receloso." 
        },
        "7": {
            "alto_desempeno": "Energía de SOCIALIZACIÓN con un enfoque en la novedad y la variedad, quienes disfrutan el cambio. En alto desempeño, estos perfiles son altamente motivados y por su personalidad tienden a ser magnéticos, dándoles gran capacidad de conectar con otros. A este perfil le gustan los proyectos, los retos que lo conecte con el disfrute y experiencias nuevas, por lo cual pueder ser muy innovadores. " ,
            "bajo_desempeno": "Energía de SOCIALIZACIÓN con un enfoque en la novedad y la variedad, quienes disfrutan el cambio. Un siete en bajo desempeño puede manifestar sentimiento de aburrición o de haber caído en una rutina lo cual le genera frustración y le puede llevar a asumir compromisos que en algun momento no quiere terminar porque no le generan emoción, deseando ir por nuevos retos y nuevas experiencias que lo conecten de nuevo con el disfrute. En bajo desempeño el eneatipo siete podría ser percibido como alguien que no quiere asumir compromisos, tener responsabilidades o ser controlado. Puede verse como como poco comprometido, con un comportamiento irreverente y cambiante, un poco desmesurado." 
        },
        "8": {
            "alto_desempeno": "Energía de LOGRO mediante la acción externa, con un alto nivel de control sobre el entorno y las personas, con mucha energía y potencial de acción enfocada. En un alto desempeño, el eneatipo 8 tiene una gran capacidad para movilizar a los otros en función del logro de los objetivos, liderando con influencia, carisma y de forma entusiasta. Puede conectar su capacidad emprendora con su influencia social para conectar con otros para su causa. En la búsqueda del objetivo involucran a otros, trabajando de forma colaborativa y brindando su guía y capacidad de visión para que entre todos se logren éstos. " ,
            "bajo_desempeno": "Energía de LOGRO mediante la acción externa, con un alto nivel de control sobre el entorno y las personas, con mucha energía y potencial de acción enfocada. Aunque el eneatipo 8 es energía de logro, en un bajo desempeño tiende a desconectarse de su entorno, a aislarse o replegarse para planear o repensar su estrategia, sin embargo lo hace desconectándose del ambiente externo, por lo cual puede bloquear el relacionamiento con otros, limitándose a controlar y dirigir, sin permitirse compartir o colaborar con otros. El bajo desempeño de este eneatipo, puede estar marcando una sensación de pérdida de control de alguna situación o del logro de sus objetivos. En bajo desempeño podría ser percibido un poco agresivo, resentido, de una fuerte exigencia, controlador, arrogante o en extremo ambicioso." 
        },
        "9": {
            "alto_desempeno": "Energía de equilibrio y con un enfoque de CONCILIACIÓN, mantiene la armonía, la paz y la estabilidad tanto a nivel interno como externo. En alto desempeño, puede movilizar a las personas siempre en un marco de justificia, buscando mediar y crear ambientes de estabilidad, siendo sin embargo capaz de desafiar su estatus quo. " ,
            "bajo_desempeno": " Energía de equilibrio y con un enfoque de CONCILIACIÓN, mantiene la armonía, la paz y la estabilidad tanto a nivel interno como externo. Sensación de caos a partir de la pérdida de su equilibro y/o paz por alguna situación que se presenta actualmente. Por su baja tolerancia al conflicto, tiende a evitarlo, por lo que podría quedarse desde una posición de queja. Aunque es una energía física, en un bajo desempeño puede decidir ""no hacer"", como un mecanismo de manifestar su inconformidad, tendiendo a aislarse de todo, ser desconfiado de su entorno." 
        }
    }
}

# Referencia a la base de datos de Firebase
ref = db.reference('Eneagrama/')

# Sube los datos a la base de datos
ref.update(datos)

# Cierra la conexión
firebase_admin.delete_app(firebase_admin.get_app())
