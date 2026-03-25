from flask import Flask, render_template, url_for

app = Flask(__name__)

FROZEN_CONFIG = {'FREEZER_DESTINATION': 'build'}
app.config.update({
    'FREEZER_DESTINATION': 'build',
    'FREEZER_BASE_URL': 'https://isaakliptzin.github.io/isaak-liptzin-website/',
})
# Reel - your main demo video
REEL_VIMEO_ID = "76979871"  # Replace with your reel's Vimeo ID

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
        "vimeo_id": "1125241996",
        "description": "2025 / 90' - Despite directing hundreds of silent films that captivated audiences from Naples to New York, Elvira Notari was relegated to the margins of film history for half a century. Her films, poised between realism and staged drama, were deeply rooted in Neapolitan folklore."
    },
    {
        "id": "doc2",
        "title": "Stonebreakers",
        "vimeo_id": "726198300",
        "description": "2022 / 70' - In a year of uprisings and political unrest, Stonebreakers documents the ongoing fights around monuments in the United States and explores the shifting landscapes of the nation's historical memory."
    },
    {
        "id": "doc3",
        "title": "If Only I Were That Warrior",
        "vimeo_id": "84273170",
        "description": "2015 / 72' - Chronicles the bloody Italian occupation of Ethiopia of 1935-1941 and examines its unresolved legacies in Italy, Ethiopia and the United States."
    },
    {
        "id": "doc4",
        "title": "Mister Wonderland",
        "vimeo_id": "366785314",
        "description": "2019 / 53' - The remarkable story of Sylvester Z. Poli, an Italian artisan who emigrated to the U.S. and became one of the greatest theater and cinema impresarios of his time."
    },
    {
        "id": "doc5",
        "title": "Iom Romì: A Day in Rome",
        "vimeo_id": "240669126",
        "description": "2017 / 30' - Chronicles a day in the life of the contemporary Jewish community of Rome, tracing its origins back to the times of the Empire."
    },
    {
        "id": "doc6",
        "title": "Treasure - The Story of Marcus Hook",
        "vimeo_id": "152448505",
        "description": "2013 / 20' - Chronicles the efforts of a community determined to survive the decline of the local refining industry through an unexpected discovery from the town's pirate past."
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
    return render_template('project.html', project=project, back_url=url_for('documentary'), back_label='Documentary')

@app.route('/news-events/')
def news_events():
    return render_template('news_events.html', projects=NEWS_EVENTS)

@app.route('/news-events/<project_id>/')
def news_event_detail(project_id):
    project = next((p for p in NEWS_EVENTS if p['id'] == project_id), None)
    if not project:
        return "Not found", 404
    return render_template('project.html', project=project, back_url=url_for('news_events'), back_label='News & Events')

@app.route('/press/')
def press():
    return render_template('press.html', press_items=PRESS_ITEMS)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
