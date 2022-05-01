import ampalibe
from conf import Configuration
from ampalibe import Payload
from requete import Requete
from ampalibe.ui import Element, Button

bot = ampalibe.init(Configuration())
chat = bot.chat
req = Requete(Configuration())
query = bot.query

print(req.list_musicAlbum(1))
@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    #----------------------------*$*---------------------------------------#
    #                    Greeting ang giving the first menu        
    #-----------------------------*$*--------------------------------------#
    chat.send_message(sender_id,"Hello hello😍😘😘😘, bienvenu dans cette espace où je vais vous partager ma musique.")
    chat.send_message(sender_id, " Bon ambiance 💖!!!")
    quick_rep = [
        {
            "content_type": "text",
            "title": 'Listes albums📀',
            "payload": Payload("/album")
        },
        {
            "content_type": "text",
            "title": 'Liste chansons🎶',
            "payload": Payload("/musique")
        },
        {
            "content_type": "text",
            "title": 'Prochaines tournées🎤',
            "payload": Payload("/tournee")
        }
    ]
    chat.send_quick_reply(sender_id, quick_rep, 'Que souhaitez-vous faire?')

@ampalibe.command('/album')
def get_album(sender_id, cmd, **extends):
    '''
        Fonction fetcher les données dans album et les afficher
    '''
    albums = req.list_album()
    data = []
    i = 0
    while i < len(albums):

        button = [
            Button(
                type="postback",
                title="Details",
                payload= Payload('/details'+ str(albums[i][0]))
            )
        ]
        data.append(
            Element(
                title= str(i+1)+ "- Album " + albums[i][1],
                image_url= albums[i][2],
                buttons= button,
            )
        )
        i = i + 1

    chat.send_template(sender_id, data, next=True)

    

@ampalibe.command('/musique')
def get_music(sender_id, cmd, **extends):
    '''
        Fonction fetcher les données dans musique et les afficher
    '''
    musiques = req.list_music()
    data = []
    i = 0
    while i < len(musiques):

        buttons = [
            Button(
                type="postback",
                title="Ecouter🎧",
                payload= Payload('/listen', id_music= str(musiques[i][0]))
            ),
            Button(
                type="postback",
                title="Regarder🎬",
                payload= Payload('/see', id_music= str(musiques[i][0]))
            ),
           
            Button(
                type="postback",
                title="Télécharger⏳",
                payload= Payload('/down_audio', id_music= str(musiques[i][0]))
            )
        ]
        data.append(
            Element(
                title= str(i+1)+ "- "+ musiques[i][1],
                image_url= musiques[i][2],
                buttons= buttons,
            )
        )
        i = i + 1

    chat.send_template(sender_id, data, next=True)
    query.set_action(sender_id, None)


@ampalibe.command('/tournee')
def get_tournee(sender_id, cmd, **extends):
    '''
        Fonction fetcher les données dans album et les afficher
    '''
    tournee = req.list_tournee()
    data = []
    i = 0
    while i < len(tournee):

        button = [
            Button(
                type="postback",
                title="Details",
                payload= Payload('/Réserver'+ str(tournee[i][0]))
            )
        ]
        data.append(
            Element(
                title= str(i+1)+ " Le " + str(tournee[i][1]) + " à " + str(tournee[i][2]) + " au " + tournee[i][3],
                image_url= tournee[i][4],
                buttons= button,
            )
        )
        i = i + 1

    chat.send_template(sender_id, data, next=True)


@ampalibe.command('/see')
def get_Video(sender_id, id_music, **extends):
    """
        Fonction pour récupérer la musique vidéo
    """

    video_name = req.get_video(id_music)
    print(video_name)
    chat.send_message(sender_id, "Enjoy it!!!")
    chat.send_file_url(sender_id, Configuration.APP_URL+f"/asset/{video_name}", filetype='video')





