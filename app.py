from flask import Flask, render_template, url_for

app = Flask(__name__)

FROZEN_CONFIG = {'FREEZER_DESTINATION': 'build'}
app.config.update({
    'FREEZER_DESTINATION': 'build',
    'FREEZER_BASE_URL': 'https://isaakliptzin.com/'
})
# Reel - your main demo video
REEL_VIMEO_ID = "1176795939"

# Sample projects data - easily editable
PROJECTS = [
    {
        "id": "project1",
        "title": "First Project",
        "vimeo_id": "76979871",
        "description": "Project description here"
    },
    {
        "id": "project2",
        "title": "Second Project",
        "vimeo_id": "76979871",
        "description": "Another project"
    },
    {
        "id": "project3",
        "title": "Third Project",
        "vimeo_id": "76979871",
        "description": "Yet another project"
    }
]

# Documentary projects
DOCUMENTARIES = [
    {
        "id": "doc1",
        "title": "Elvira Notari: Beyond Silence",
        "meta": "2025 / 90'",
        "vimeo_id": "1125241996",
        "description": "Between 1906 and 1930, Elvira Notari directed over 60 films from Naples — yet spent half a century erased from film history. This documentary recovers her legacy, tracing a singular voice working at the intersection of melodrama and Neapolitan street life."
    },
    {
        "id": "doc2",
        "title": "Stonebreakers",
        "meta": "2022 / 70'",
        "vimeo_id": "726198300",
        "description": "Shot during and after the 2020 uprisings, Stonebreakers surveys the nationwide fight over monuments to Confederate leaders, Columbus, and other contested figures — examining how Americans on all sides negotiate historical memory and the legacies of slavery and colonialism."
    },
    {
        "id": "doc3",
        "title": "If Only I Were That Warrior",
        "meta": "2015 / 72'",
        "vimeo_id": "84273170",
        "description": "When an Italian village erected a monument to General Graziani — Mussolini's 'Butcher of Ethiopia' — it exposed a silence decades in the making. Following subjects across Italy, Ethiopia, and the U.S., the film examines a colonial past the country has never fully reckoned with."
    },
    {
        "id": "doc4",
        "title": "Mister Wonderland",
        "meta": "2019 / 53'",
        "vimeo_id": "366785314",
        "description": "Born near Lucca, Sylvester Z. Poli emigrated to America and built a theater empire spanning more than 30 venues across the Northeast, booking legends from Houdini to Mae West — tracing the unlikely arc from immigrant artisan to powerful showman."
    },
    {
        "id": "doc5",
        "title": "Iom Romì: A Day in Rome",
        "meta": "2017 / 30'",
        "vimeo_id": "240669126",
        "description": "From dawn to dusk in Rome's ancient Ghetto, the film follows members of a community whose presence in the city stretches back to the age of the Empire — tracing what it means to be simultaneously Roman and Jewish today."
    },
    {
        "id": "doc6",
        "title": "Treasure - The Story of Marcus Hook",
        "meta": "2013 / 20'",
        "vimeo_id": "152448505",
        "description": "After the Sunoco refinery closed in 2011, Marcus Hook, Pennsylvania faced an uncertain future. The film follows a former refinery worker who unearthed what may be the home of Blackbeard's mistress — and channeled that discovery into a pirate festival that revived the town."
    }
]

# News & Events
NEWS_EVENTS = [
    {
        "id": "news1",
        "title": "Opera Italiana is in the Air - Washington DC 2024",
        "vimeo_id": "954479835",
        "description": "News/Event description"
    },
    {
        "id": "news2",
        "title": "The Batman of the Hudson",
        "vimeo_id": "135837829",
        "description": "News/Event description"
    },
    {
        "id": "news3",
        "title": "The Battle For New York Series",
        "vimeo_id": "253910875",
        "description": "News/Event description"
    }
]

# Press items
PRESS_ITEMS = [
    {
        "outlet": "Variety",
        "year": "2025",
        "title": "'Elvira Notari: Beyond Silence' Acquired by First Hand Films Ahead of Venice Premiere",
        "url": "https://variety.com/2025/film/global/elvira-notari-beyond-silence-female-film-first-hand-venice-1236501705/",
        "description": "Variety covers the world sales acquisition of Awen Films' documentary on Italy's first female director, co-produced and shot by Liptzin, premiering at the 82nd Venice International Film Festival."
    },
    {
        "outlet": "La Voce di New York",
        "year": "2025",
        "title": "Pioneer Woman Italian Director Elvira Notari Back from the Shadows at Venice 82",
        "url": "https://lavocedinewyork.com/en/arts/2025/07/29/pioneer-woman-italian-director-elvira-notari-back-from-the-shadows-at-venice-82/",
        "description": "Profile of the documentary premiering at Venice Classics, produced and shot by Liptzin alongside director Valerio Ciriaci for Awen Films."
    },
    {
        "outlet": "L'Italo Americano",
        "year": "2025",
        "title": "The Forgotten Cinema of Elvira Notari",
        "url": "https://italoamericano.org/elvira-notari-forgotten-cinema/",
        "description": "Feature on the Venice-bound documentary, with references to Liptzin as co-founder of Awen Films and cinematographer on the project."
    },
    {
        "outlet": "Venice Biennale Cinema",
        "year": "2025",
        "title": "Biennale Cinema 2025 — Elvira Notari: Beyond Silence (Official Selection)",
        "url": "https://www.labiennale.org/en/cinema/2025/venice-classics/elvira-notari-oltre-il-silenzio",
        "description": "Official Venice Film Festival listing for the documentary produced by Liptzin and Awen Films, selected for the Venice Classics section."
    },
    {
        "outlet": "Katie at the Movies",
        "year": "2025",
        "title": "Venice 2025 Review: 'Elvira Notari: Beyond Silence'",
        "url": "https://katieatthemovies.com/2025/09/03/venice-2025-elvira-notari-beyond-silence/",
        "description": "Festival review of the documentary Liptzin co-produced and shot, praised for its engaging portrait of the forgotten silent-era pioneer."
    },
    {
        "outlet": "Bay State Banner",
        "year": "2023",
        "title": "'Stonebreakers' Chronicles Toppling of Controversial Monuments Against Backdrop of BLM Protests",
        "url": "https://baystatebanner.com/2023/04/26/stonebreakers-chronicles-toppling-of-controversial-monuments-against-backdrop-of-blm-protests/",
        "description": "Interview with Liptzin and director Valerio Ciriaci ahead of the U.S. premiere at IFFBoston, covering the film's cross-country production."
    },
    {
        "outlet": "ArtsEmerson",
        "year": "2023",
        "title": "Stonebreakers — Filmmaker Feature",
        "url": "https://artsemerson.org/events/stonebreakers/",
        "description": "Filmmaker profile accompanying the Boston screening, detailing Liptzin's role as producer and cinematographer on the award-winning documentary."
    },
    {
        "outlet": "Montclair State University",
        "year": "2023",
        "title": "Stonebreakers: Documentary Screening & Q&A with Valerio Ciriaci and Isaak J. Liptzin",
        "url": "https://www.montclair.edu/inserra-chair/events/2023-24-events/stonebreakers/",
        "description": "Inserra Chair event page for the Montclair State screening and post-film discussion with Liptzin and Ciriaci."
    },
    {
        "outlet": "UC Santa Barbara / Carsey-Wolf Center",
        "year": "2023",
        "title": "CWC Docs: Stonebreakers — Screening & Discussion",
        "url": "https://www.carseywolf.ucsb.edu/pollock-events/stonebreakers/",
        "description": "Post-screening discussion event with Liptzin and Ciriaci at UC Santa Barbara, moderated by Stephanie Malia Hom."
    },
    {
        "outlet": "UCTV",
        "year": "2023",
        "title": "CWC Docs: Stonebreakers — Filmed Discussion",
        "url": "https://www.uctv.tv/shows/39636",
        "description": "Recorded conversation in which Liptzin and Ciriaci discuss the origins of Stonebreakers, filming protests, and documentary's tension between history and memory."
    },
    {
        "outlet": "BroadwayWorld",
        "year": "2022",
        "title": "Palace Theater Waterbury Presents Free Screening of MISTER WONDERLAND",
        "url": "https://www.broadwayworld.com/connecticut/article/Palace-Theater-Waterbury-Presents-Free-Movie-Screening-Of-MISTER-WONDERLAND-20220113",
        "description": "Coverage of the Connecticut screening of Liptzin's documentary on Italian-American theater magnate S.Z. Poli."
    },
    {
        "outlet": "La Voce di New York",
        "year": "2020",
        "title": "Mr. Wonderland: An Immigrant's Life Finally Rediscovered and Celebrated",
        "url": "https://lavocedinewyork.com/en/arts/2020/12/05/mr-wonderland-an-immigrants-life-finally-rediscovered-and-celebrated/",
        "description": "Feature on the PBS/CPTV debut of Mister Wonderland, produced and shot by Liptzin, tracing the forgotten story of Italian-American showman S.Z. Poli."
    },
    {
        "outlet": "iItaly",
        "year": "2018",
        "title": "Iom Romì (A Day in Rome) Debuts for an American Audience",
        "url": "http://www.iitaly.org/magazine/focus/art-culture/article/iom-romi-day-in-rome-debuts-american-audience",
        "description": "Review and Q&A recap of the New York Jewish Film Festival screening; Liptzin speaks about producing the short documentary on Rome's Jewish community."
    },
    {
        "outlet": "JFilmBox",
        "year": "2018",
        "title": "Filmmaker Profile: Isaak Liptzin",
        "url": "https://jfilmbox.org/film-maker/isaak-liptzin/",
        "description": "Career overview of Liptzin's work spanning WNYC photojournalism, Awen Films, RAI presidential coverage, and the Netflix series First Team: Juventus."
    },
    {
        "outlet": "Tadias Magazine",
        "year": "2016",
        "title": "Interview with the Director & Producer of 'If Only I Were That Warrior'",
        "url": "http://www.tadias.com/05/23/2016/interview-with-the-director-producer-of-if-only-i-were-that-warrior/",
        "description": "In-depth interview with Liptzin and director Ciriaci on making the Italian Golden Globe–winning documentary about the Graziani monument controversy."
    },
    {
        "outlet": "Tadias Magazine",
        "year": "2016",
        "title": "Ethiopia–Italy Film 'If Only I Were That Warrior' Released on DVD",
        "url": "http://www.tadias.com/11/14/2016/ethiopia-film-on-italy-rise-of-fascism-if-only-i-were-that-warrior-on-dvd/",
        "description": "Coverage of the DVD and streaming release of the documentary, quoting Liptzin on the film's goal of raising awareness about Italian historical revisionism."
    },
    {
        "outlet": "WNYC",
        "year": "2015",
        "title": "Isaak Liptzin — Contributor, WNYC New York Public Radio",
        "url": "https://www.wnyc.org/people/isaak-liptzin/",
        "description": "Liptzin's byline page at WNYC, where he contributed photojournalism on NYC housing, arts, and culture including Times Square student art and MTA musicians."
    }
]


@app.route('/')
def index():
    return render_template('index.html', reel_vimeo_id=REEL_VIMEO_ID)

@app.route('/documentary/')
def documentary():
    return render_template('documentary.html', projects=DOCUMENTARIES)

@app.route('/documentary/<project_id>/')
def documentary_detail(project_id):
    project = next((p for p in DOCUMENTARIES if p['id'] == project_id), None)
    if not project:
        return "Not found", 404
    return render_template('project.html', project=project, back_url=url_for('documentary'), back_label='Films')

@app.route('/news-events/')
def news_events():
    return render_template('news_events.html', projects=NEWS_EVENTS)

@app.route('/news-events/<project_id>/')
def news_event_detail(project_id):
    project = next((p for p in NEWS_EVENTS if p['id'] == project_id), None)
    if not project:
        return "Not found", 404
    return render_template('project.html', project=project, back_url=url_for('news_events'), back_label='News & Events')

@app.route('/media/')
def press():
    return render_template('press.html', press_items=PRESS_ITEMS)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
