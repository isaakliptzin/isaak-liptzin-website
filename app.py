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
        "description": "<em>Elvira Notari: Beyond Silence</em> resurrects the legacy of Italy's first female director, a prolific pioneer whose Neapolitan silent films survived Fascist censorship and historical neglect to inspire a new generation of artists."
    },
    {
        "id": "doc2",
        "title": "Stonebreakers",
        "meta": "2022 / 70'",
        "vimeo_id": "726198300",
        "description": "<em>Stonebreakers</em> chronicles the 2020 uprisings against U.S. monuments, interrogating the fall of national myths and the urgent link between historical memory and modern political action."
    },
    {
        "id": "doc3",
        "title": "If Only I Were That Warrior",
        "meta": "2015 / 72'",
        "vimeo_id": "84273170",
        "description": "<em>If Only I Were That Warrior</em> explores the unpunished war crimes of Italy's 1935 occupation of Ethiopia, tracing how a modern monument to a Fascist general reignites a painful legacy across the history of two nations and their diaspora."
    },
    {
        "id": "doc4",
        "title": "Mister Wonderland",
        "meta": "2019 / 53'",
        "vimeo_id": "366785314",
        "description": "<em>Mister Wonderland</em> follows the journey of Sylvester Z. Poli, a humble artisan from Tuscany who emigrated to America to become the greatest theater impresario of his era, revealing how a migrant's ingenuity defined the modern movie-going experience."
    },
    {
        "id": "doc5",
        "title": "Iom Romì: A Day in Rome",
        "meta": "2017 / 30'",
        "vimeo_id": "240669126",
        "description": "<em>Iom Romì</em> chronicles a day in the life of Rome's Jewish community, the city's oldest continuous cultural lineage, capturing the unique rituals and fierce independence of a people existing for centuries between persecution and integration."
    },
    {
        "id": "doc6",
        "title": "Treasure - The Story of Marcus Hook",
        "meta": "2013 / 20'",
        "vimeo_id": "152448505",
        "description": "<em>Treasure</em> follows a Pennsylvania refinery town on the brink of collapse, where an unexpected discovery of pirate history sparks a quest for reinvention and explores what it means for a community to survive deindustrialization."
    }
]

# Other Work
NEWS_EVENTS = [
    {
        "id": "ow1",
        "title": "First Team: Juventus",
        "embed_url": "https://www.youtube-nocookie.com/embed/VYAFpdgH8oo?rel=0&iv_load_policy=3&modestbranding=1",
        "description": "Netflix Originals"
    },
    {
        "id": "ow2",
        "title": "Undocumented During COVID-19",
        "embed_url": "https://www.youtube-nocookie.com/embed/HlCrudEfGFs?rel=0&iv_load_policy=3&modestbranding=1",
        "description": "AJ+"
    },
    {
        "id": "ow3",
        "title": "The Mutation - Walking with Manzoni",
        "embed_url": "https://www.youtube-nocookie.com/embed/MD32CHm5UQU?rel=0&iv_load_policy=3&modestbranding=1",
        "description": "NYU Casa Italiana Zerilli-Marimò"
    },
    {
        "id": "ow4",
        "title": "Michael Kors F/W 2026",
        "embed_url": "https://player.vimeo.com/video/1168594003",
        "description": ""
    },
    {
        "id": "ow5",
        "title": "The Batman of the Hudson",
        "embed_url": "https://player.vimeo.com/video/341674106",
        "description": "MSNBC"
    },
    {
        "id": "ow6",
        "title": "Persisting Matters - Michael Rakowitz",
        "embed_url": "https://player.vimeo.com/video/952025124?h=3e8a2777ed",
        "description": "Center for Italian Modern Art"
    },
    {
        "id": "ow7",
        "title": "Statuesque",
        "embed_url": "https://www.youtube-nocookie.com/embed/Lm4ObZR7mc0?rel=0&iv_load_policy=3&modestbranding=1",
        "description": "Italian Cultural Institute in DC"
    },
    {
        "id": "ow8",
        "title": "Tracking the Tide",
        "embed_url": "https://player.vimeo.com/video/1067887543?h=c69ac5b2a6",
        "description": "Global Fishing Watch"
    },
    {
        "id": "ow9",
        "title": "Research and Conservation at The Met",
        "embed_url": "https://player.vimeo.com/video/797136736?h=14fde35c7b",
        "description": "Foreign Ministry of Italy"
    },
    {
        "id": "ow10",
        "title": "Re-Writing History",
        "embed_url": "https://www.youtube-nocookie.com/embed/9WPMpeMDJBQ?rel=0&iv_load_policy=3&modestbranding=1",
        "description": "The Andrew Freedman Home"
    },
    {
        "id": "ow11",
        "title": "Louis Vuitton Cruise 2019",
        "embed_url": "https://player.vimeo.com/video/335912497",
        "description": ""
    },
    {
        "id": "ow12",
        "title": "A Serenade at Sunset",
        "embed_url": "https://player.vimeo.com/video/954479835?h=52aff22ae2",
        "description": "Opera Italiana is in the Air"
    },
    {
        "id": "ow13",
        "title": "Ralph Lauren Fall 2026",
        "embed_url": "https://player.vimeo.com/video/1168654185",
        "description": ""
    },
    {
        "id": "ow14",
        "title": "I'm Counting on You, on Everyone",
        "embed_url": "https://player.vimeo.com/video/199056338",
        "description": "Centro Primo Levi"
    }
]

# Press items
PRESS_ITEMS = [
    {
        "outlet": "Variety",
        "year": "2025",
        "title": "'Elvira Notari: Beyond Silence' Acquired by First Hand Films Ahead of Venice Premiere",
        "url": "https://variety.com/2025/film/global/elvira-notari-beyond-silence-female-film-first-hand-venice-1236501705/",
        "description": "Article detailing the world sales acquisition of <em>Elvira Notari: Beyond Silence</em> by First Hand Films ahead of its premiere at the 82nd Venice International Film Festival."
    },
    {
        "outlet": "WBUR",
        "year": "2023",
        "title": "Stonebreakers Puts Monuments Under the Microscope",
        "url": "https://www.wbur.org/radioboston/2023/04/28/thanksgiving-christopher-columbus-native-americans",
        "description": "Boston Public Radio segment on <em>Stonebreakers</em> and the debates surrounding monuments to Columbus, Mount Rushmore, and other contested American landmarks, featuring an interview with Isaak Liptzin."
    },
    {
        "outlet": "Bay State Banner",
        "year": "2023",
        "title": "'Stonebreakers' Chronicles Toppling of Controversial Monuments Against Backdrop of BLM Protests",
        "url": "https://baystatebanner.com/2023/04/26/stonebreakers-chronicles-toppling-of-controversial-monuments-against-backdrop-of-blm-protests/",
        "description": "Interview with Isaak Liptzin and director Valerio Ciriaci ahead of the U.S. premiere of <em>Stonebreakers</em> at IFFBoston, covering the film's cross-country production."
    },
    {
        "outlet": "Venice Biennale Cinema",
        "year": "2025",
        "title": "Biennale Cinema 2025 — Elvira Notari: Beyond Silence (Official Selection)",
        "url": "https://www.labiennale.org/en/cinema/2025/venice-classics/elvira-notari-oltre-il-silenzio",
        "description": "Official Venice Film Festival listing for <em>Elvira Notari: Beyond Silence</em>, selected for the Venice Classics section."
    },
    {
        "outlet": "UC Santa Barbara / Carsey-Wolf Center",
        "year": "2023",
        "title": "CWC Docs: Stonebreakers — Screening & Discussion",
        "url": "https://www.carseywolf.ucsb.edu/pollock-events/stonebreakers/",
        "description": "Post-screening Q&A with Isaak Liptzin and Valerio Ciriaci at UC Santa Barbara, moderated by Stephanie Malia Hom."
    },
    {
        "outlet": "La Voce di New York",
        "year": "2025",
        "title": "Pioneer Woman Italian Director Elvira Notari Back from the Shadows at Venice 82",
        "url": "https://lavocedinewyork.com/en/arts/2025/07/29/pioneer-woman-italian-director-elvira-notari-back-from-the-shadows-at-venice-82/",
        "description": "Profile of <em>Elvira Notari: Beyond Silence</em> ahead of its Venice Classics premiere."
    },
    {
        "outlet": "L'Italo Americano",
        "year": "2025",
        "title": "The Forgotten Cinema of Elvira Notari",
        "url": "https://italoamericano.org/elvira-notari-forgotten-cinema/",
        "description": "Feature on <em>Elvira Notari: Beyond Silence</em> ahead of its Venice premiere."
    },
    {
        "outlet": "Katie at the Movies",
        "year": "2025",
        "title": "Venice 2025 Review: 'Elvira Notari: Beyond Silence'",
        "url": "https://katieatthemovies.com/2025/09/03/venice-2025-elvira-notari-beyond-silence/",
        "description": "Festival review of <em>Elvira Notari: Beyond Silence</em> from the Venice premiere."
    },
    {
        "outlet": "YES! Magazine",
        "year": "2024",
        "title": "Monumental Shifts",
        "url": "https://www.yesmagazine.org/issue/truth/2024/09/04/monumental-shifts",
        "description": "Feature tracing how Isaak Liptzin and Valerio Ciriaci expanded <em>Stonebreakers</em> from a Columbus-focused project into a broader examination of contested monuments following the 2020 uprisings."
    },
    {
        "outlet": "Princeton University",
        "year": "2024",
        "title": "Screening of 'Stonebreakers' by Valerio Ciriaci",
        "url": "https://fit.princeton.edu/events/screening-stonebreakers-valerio-ciriaci",
        "description": "Screening of <em>Stonebreakers</em> at Princeton's Department of French and Italian, followed by a Q&A with Isaak Liptzin, Valerio Ciriaci, and Princeton professor Kinohi Nishikawa."
    },
    {
        "outlet": "University of Cambridge",
        "year": "2024",
        "title": "'Stonebreakers' Screening — Award-Winning Documentary on Conflicts Over Monuments",
        "url": "https://www.english.cam.ac.uk/news/archives/8231",
        "description": "Screening of <em>Stonebreakers</em> at the University of Cambridge Faculty of English, followed by a discussion with the filmmakers."
    },
    {
        "outlet": "Video Librarian",
        "year": "2024",
        "title": "Stonebreakers — Documentary Review",
        "url": "https://videolibrarian.com/reviews/documentary/the-stonebreakers/",
        "description": "Trade review of <em>Stonebreakers</em>, examining the film's portrait of contested monuments and the communities calling for historical reckoning."
    },
    {
        "outlet": "Montclair State University",
        "year": "2023",
        "title": "Stonebreakers: Documentary Screening & Q&A with Valerio Ciriaci and Isaak J. Liptzin",
        "url": "https://www.montclair.edu/inserra-chair/events/2023-24-events/stonebreakers/",
        "description": "Event page for the Montclair State screening and Q&A with Isaak Liptzin and Valerio Ciriaci."
    },
    {
        "outlet": "ArtsEmerson",
        "year": "2023",
        "title": "Stonebreakers — Boston Screening & Q&A",
        "url": "https://artsemerson.org/events/stonebreakers/",
        "description": "ArtsEmerson event page for the Boston theatrical run of <em>Stonebreakers</em>, with Isaak Liptzin and Valerio Ciriaci in attendance."
    },
    {
        "outlet": "La Voce di New York",
        "year": "2020",
        "title": "Mr. Wonderland: An Immigrant's Life Finally Rediscovered and Celebrated",
        "url": "https://lavocedinewyork.com/en/arts/2020/12/05/mr-wonderland-an-immigrants-life-finally-rediscovered-and-celebrated/",
        "description": "Feature on the PBS/CPTV debut of <em>Mister Wonderland</em>, tracing the forgotten story of Italian-American showman S.Z. Poli."
    },
    {
        "outlet": "BroadwayWorld",
        "year": "2022",
        "title": "Palace Theater Waterbury Presents Free Screening of MISTER WONDERLAND",
        "url": "https://www.broadwayworld.com/connecticut/article/Palace-Theater-Waterbury-Presents-Free-Movie-Screening-Of-MISTER-WONDERLAND-20220113",
        "description": "Coverage of a free screening of <em>Mister Wonderland</em> at the Palace Theater Waterbury, Connecticut."
    },
    {
        "outlet": "iItaly",
        "year": "2018",
        "title": "Iom Romì (A Day in Rome) Debuts for an American Audience",
        "url": "http://www.iitaly.org/magazine/focus/art-culture/article/iom-romi-day-in-rome-debuts-american-audience",
        "description": "Review and Q&A recap from the New York Jewish Film Festival screening of <em>Iom Romì</em>, with Isaak Liptzin discussing the film's production."
    },
    {
        "outlet": "JFilmBox",
        "year": "2018",
        "title": "Filmmaker Profile: Isaak Liptzin",
        "url": "https://jfilmbox.org/film-maker/isaak-liptzin/",
        "description": "Career profile of Isaak Liptzin spanning WNYC photojournalism, Awen Films, RAI presidential coverage, and the Netflix series <em>First Team: Juventus</em>."
    },
    {
        "outlet": "Tadias Magazine",
        "year": "2016",
        "title": "Interview with the Director & Producer of 'If Only I Were That Warrior'",
        "url": "http://www.tadias.com/05/23/2016/interview-with-the-director-producer-of-if-only-i-were-that-warrior/",
        "description": "In-depth interview with Isaak Liptzin and Valerio Ciriaci on making the Italian Golden Globe–winning documentary about the Graziani monument controversy."
    },
    {
        "outlet": "WNYC",
        "year": "2015",
        "title": "Isaak Liptzin — Contributor, WNYC New York Public Radio",
        "url": "https://www.wnyc.org/people/isaak-liptzin/",
        "description": "Isaak Liptzin's contributor page at WNYC, where he covered NYC housing, arts, and culture."
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
    return render_template('project.html', project=project, back_url=url_for('news_events'), back_label='Other Work')

@app.route('/media/')
def press():
    return render_template('press.html', press_items=PRESS_ITEMS)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
