import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Drop table if already exists (to avoid duplicate errors)
cursor.execute("DROP TABLE IF EXISTS books")

# Create books table
cursor.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stress_type TEXT,
    title TEXT,
    author TEXT,
    chapter TEXT,
    content TEXT,
    shelf TEXT,
    availability TEXT,
    priority INTEGER
)
""")

# Insert sample books
books = [
    ("academic",
     "Deep Work",
     "Cal Newport",
     "Chapter 3: Focus Rules",
     """In Chapter 3 of 'Deep Work,' Cal Newport delves into the concept of 'focus rules,' which are essential strategies for cultivating deep concentration in an academic setting. The chapter begins by explaining why deep work is crucial for students and researchers alike. Newport argues that in a world filled with distractions, the ability to focus intensely on cognitively demanding tasks is a superpower that leads to higher productivity and better academic outcomes.

He introduces the idea that deep work requires deliberate practice and specific rules to protect one's attention. One key rule is to schedule deep work sessions in advance, treating them as non-negotiable appointments. This helps in building a routine where the brain expects and prepares for focused effort.

Newport discusses the importance of creating rituals around deep work. For instance, he suggests starting each session with a clear goal, minimizing distractions by working in a quiet environment, and even using tools like noise-canceling headphones or apps that block social media. These rituals signal to the brain that it's time to enter a state of deep focus.

The chapter also addresses the myth that multitasking is efficient. Newport provides evidence from neuroscience showing that switching between tasks depletes mental energy and reduces overall performance. He encourages students to embrace monotasking, dedicating uninterrupted time to studying or research.

Furthermore, Newport explores the role of willpower in maintaining focus. He explains that willpower is like a muscle that can be trained but also fatigued. To sustain deep work, one must manage energy levels by taking breaks, exercising, and ensuring adequate sleep.

He shares examples of successful academics who have implemented focus rules, such as Nobel laureates who isolated themselves for long periods to make breakthroughs. This illustrates how deep work can lead to significant achievements in academia.

The chapter concludes by emphasizing that while deep work is challenging, the rewards—reduced stress from procrastination, better grades, and a sense of accomplishment—are worth the effort. Newport encourages readers to start small, perhaps with 90-minute focused sessions, and gradually build up their capacity for deep concentration.

Overall, this chapter equips students with practical tools to combat academic stress by fostering a disciplined approach to focus, ultimately leading to more meaningful and productive learning experiences.""",
     "A1",
     "Available"),

    ("anxiety",
     "The Anxiety and Phobia Workbook",
     "Edmund Bourne",
     "Chapter 5: Relaxation Techniques",
     """Chapter 5 of 'The Anxiety and Phobia Workbook' by Edmund Bourne focuses on relaxation techniques as a fundamental tool for managing anxiety symptoms. Bourne starts by explaining the physiological basis of anxiety, how the body's stress response can be triggered by perceived threats, leading to symptoms like rapid heartbeat, sweating, and muscle tension.

He introduces progressive muscle relaxation (PMR), a technique where individuals tense and then relax different muscle groups systematically. This method helps in releasing physical tension and promotes a sense of calm. Bourne provides step-by-step instructions, suggesting starting from the toes and working up to the head, spending time on each muscle group.

The chapter also covers deep breathing exercises, emphasizing diaphragmatic breathing to counteract shallow, anxious breathing. Bourne teaches readers to inhale slowly through the nose, hold for a few seconds, and exhale through the mouth, which activates the parasympathetic nervous system and reduces anxiety.

Visualization and guided imagery are another key technique discussed. Bourne guides readers to imagine peaceful scenes, such as a serene beach or forest, to distract from anxious thoughts and induce relaxation. He includes scripts for self-guided sessions.

Autogenic training is introduced as a self-hypnosis method where individuals repeat phrases like 'My arms are heavy and warm' to achieve deep relaxation. Bourne explains how this can lower heart rate and blood pressure.

The chapter addresses common barriers to relaxation, such as impatience or skepticism, and offers tips to overcome them, like practicing daily and combining techniques.

Bourne shares case studies of individuals who have successfully used these methods to reduce panic attacks and generalized anxiety. He stresses the importance of consistency, recommending 15-20 minutes of practice daily.

Finally, he integrates relaxation with cognitive techniques, suggesting using relaxation to create a safe space for challenging anxious thoughts. This holistic approach empowers readers to take control of their anxiety through accessible, evidence-based methods.""",
     "B2",
     "Available"),

    ("emotional",
     "Feeling Good",
     "David Burns",
     "Chapter 2: Mood Therapy",
     """In Chapter 2 of 'Feeling Good,' David Burns introduces the concept of mood therapy, a cognitive approach to understanding and overcoming sadness and negative emotions. He begins by challenging the common belief that feelings are caused by external events, instead proposing that thoughts and interpretations shape our emotional responses.

Burns explains the cognitive triad: negative views about oneself, the world, and the future that perpetuate depression. He illustrates this with examples, such as how a rejection can lead to thoughts like 'I'm worthless,' amplifying sadness.

The chapter delves into cognitive distortions, common thinking errors like all-or-nothing thinking, overgeneralization, and catastrophizing. Burns provides examples and encourages readers to identify these patterns in their own thinking.

He introduces the Daily Mood Log, a tool for tracking negative thoughts, associated emotions, and evidence for and against them. This helps in disputing irrational beliefs and replacing them with balanced alternatives.

Burns discusses the role of underlying assumptions and core beliefs in maintaining negative moods. He guides readers to uncover beliefs like 'I must be perfect' and challenge them.

The chapter includes exercises for reframing negative thoughts, such as writing compassionate responses to self-criticism. Burns emphasizes that changing thoughts can directly improve mood.

He addresses the resistance some feel toward cognitive therapy, reassuring that it's a skill that improves with practice. Case studies demonstrate how mood therapy has helped individuals overcome severe depression.

Burns concludes by highlighting the empowering nature of mood therapy, giving individuals control over their emotional well-being rather than feeling victimized by circumstances.""",
     "C3",
     "Available"),

    ("family",
     "Boundaries",
     "Henry Cloud",
     "Chapter 4: Family Relationships",
     """Chapter 4 of 'Boundaries' by Henry Cloud explores the complexities of family relationships and the importance of setting healthy boundaries to manage pressure and maintain inner peace. Cloud starts by acknowledging that family dynamics are often intense due to shared history and expectations.

He defines boundaries as personal property lines that define where one person ends and another begins. In families, blurred boundaries can lead to enmeshment, where individuals lose their sense of self.

Cloud discusses common family issues like codependency, where one member's behavior controls another's emotions. He explains how setting boundaries can prevent this by allowing each person to take responsibility for their own feelings and actions.

The chapter provides practical advice on communicating boundaries, such as using 'I' statements to express needs without blame. For example, 'I feel overwhelmed when...' instead of 'You always...'

Cloud addresses resistance from family members, suggesting that boundaries may initially cause conflict but ultimately lead to healthier relationships. He encourages persistence and self-care during this process.

He shares biblical and psychological insights on love and limits, arguing that true love involves both grace and truth, including the ability to say no.

Case studies illustrate how boundaries have transformed dysfunctional family systems, reducing stress and improving communication.

The chapter concludes by emphasizing that boundaries are not walls but bridges that allow for deeper, more authentic connections. Cloud motivates readers to prioritize their well-being while honoring family ties.""",
     "D1",
     "Available"),

    ("confidence",
     "The Confidence Code",
     "Katty Kay",
     "Chapter 6: Building Self-Trust",
     """In Chapter 6 of 'The Confidence Code,' Katty Kay and Claire Shipman focus on building self-trust as a foundation for confidence. They explain that self-trust is the belief in one's ability to handle challenges, which differs from self-esteem.

The authors discuss how self-trust develops through experiences of overcoming obstacles. They encourage readers to reflect on past successes and learn from failures without self-judgment.

Kay and Shipman introduce the concept of 'confidence loops,' where small acts of courage build momentum. They suggest starting with low-stakes actions, like speaking up in meetings, to reinforce self-trust.

The chapter addresses imposter syndrome, common among high-achievers, and provides strategies to combat it, such as reframing thoughts and seeking mentorship.

They emphasize the role of vulnerability in building trust, sharing stories of leaders who admitted mistakes to gain credibility.

Practical exercises include journaling about strengths and setting achievable goals to practice self-trust.

The authors highlight gender differences, noting that women often undervalue their abilities, and urge building self-trust to close this gap.

Case studies of confident individuals demonstrate how self-trust leads to resilience and success.

The chapter concludes by affirming that self-trust is a skill that can be cultivated, leading to a more confident and fulfilling life.""",
     "E2",
     "Available"),

    ("social",
     "How to Win Friends and Influence People",
     "Dale Carnegie",
     "Chapter 1: Fundamental Techniques in Handling People",
     """Chapter 1 of 'How to Win Friends and Influence People' by Dale Carnegie lays the foundation for effective interpersonal skills. Carnegie begins by stating that success in life depends largely on one's ability to deal with people.

He introduces the principle of not criticizing, condemning, or complaining, as these create defensiveness. Instead, he advocates understanding others' perspectives and appreciating their viewpoints.

Carnegie emphasizes the importance of genuine interest in others. He suggests remembering names, listening actively, and asking questions to show care.

The chapter discusses how people are motivated by their desires, not ours. Carnegie advises talking about what the other person wants and showing how it benefits them.

He shares anecdotes, like how a smile and a kind word changed outcomes in difficult situations.

Carnegie warns against arguments, explaining that winning an argument often means losing a friend. He promotes finding common ground.

The chapter includes tips for making others feel important, such as sincere compliments and encouragement.

Carnegie concludes that these techniques reduce social stress by fostering positive relationships, leading to personal and professional success.""",
     "F1",
     "Available"),

    ("loneliness",
     "Loneliness: Human Nature and the Need for Social Connection",
     "John Cacioppo",
     "Chapter 7: The Science of Loneliness",
     """Chapter 7 of 'Loneliness' by John Cacioppo explores the scientific underpinnings of loneliness and its impact on health. Cacioppo defines loneliness as the discrepancy between desired and actual social connections.

He presents research showing loneliness activates the same stress responses as physical pain, leading to increased cortisol and weakened immunity.

The chapter discusses evolutionary aspects, how humans are wired for social bonds, and how modern life disrupts them.

Cacioppo introduces the concept of perceived social isolation, which can occur even in crowds, and its link to depression and anxiety.

He explains neural pathways involved, including the role of oxytocin and dopamine in social bonding.

Strategies for fostering connections include quality over quantity, such as deep conversations and shared activities.

Cacioppo shares studies on interventions like social skills training and community involvement that reduce loneliness.

The chapter addresses cultural factors, noting how individualism in some societies exacerbates isolation.

He concludes by emphasizing that addressing loneliness is crucial for public health, promoting policies and personal efforts to build meaningful connections.""",
     "G3",
     "Available"),

    ("breakup",
     "It's Called a Breakup Because It's Broken",
     "Greg Behrendt",
     "Chapter 5: Moving On",
     """Chapter 5 of 'It's Called a Breakup Because It's Broken' by Greg Behrendt provides practical advice for healing and moving forward after a breakup. Behrendt starts by acknowledging the pain of loss and the importance of grieving.

He advises against immediate rebounds, suggesting time to process emotions. He encourages activities like journaling or therapy to work through feelings.

Behrendt discusses rebuilding self-identity, reminding readers that breakups end relationships, not lives. He promotes rediscovering hobbies and interests.

The chapter covers letting go of resentment, using techniques like forgiveness exercises to free oneself emotionally.

Behrendt shares stories of people who transformed breakups into opportunities for growth, such as career changes or travel.

He warns against idealizing the ex-partner and encourages focusing on personal flaws in the relationship.

Practical steps include creating a support network and setting new goals.

The chapter concludes by affirming that healing takes time but leads to stronger, more authentic futures.""",
     "H1",
     "Available"),

    ("financial",
     "Your Money or Your Life",
     "Vicki Robin",
     "Chapter 1: The First Step",
     """Chapter 1 of 'Your Money or Your Life' by Vicki Robin introduces the transformative approach to money management. Robin challenges the cultural obsession with wealth, proposing that true financial independence comes from aligning money with life values.

She explains the 'money myth,' where more income is seen as the solution to happiness, leading to endless cycles of work and spend.

Robin guides readers to track every expense to understand their money flow and identify leaks.

The chapter discusses the concept of 'enough,' encouraging sufficiency over excess.

She introduces the idea of life energy, viewing time as currency and questioning if jobs truly fulfill.

Robin shares personal stories of individuals who broke free from financial stress through mindful spending.

The chapter concludes by inviting readers to rethink their relationship with money for greater peace and purpose.""",
     "I1",
     "Available"),

    ("health",
     "The Blue Zones",
     "Dan Buettner",
     "Chapter 3: Move Naturally",
     """Chapter 3 of 'The Blue Zones' by Dan Buettner explores how natural movement reduces stress and promotes longevity. Buettner draws from centenarian communities where physical activity is integrated into daily life.

He explains that modern sedentary lifestyles contribute to health issues, contrasting with ancestral movement patterns.

The chapter details benefits of activities like walking, gardening, and manual labor in lowering stress hormones.

Buettner provides tips for incorporating natural movement, such as standing desks or walking meetings.

He shares research on how exercise boosts endorphins and improves mental health.

Case studies from Blue Zones illustrate how movement fosters community and reduces isolation.

The chapter concludes by urging readers to make movement enjoyable and sustainable for long-term health.""",
     "J2",
     "Available"),

    ("career",
     "Designing Your Life",
     "Bill Burnett",
     "Chapter 2: Building a Compass",
     """Chapter 2 of 'Designing Your Life' by Bill Burnett and Dave Evans helps readers clarify values and passions to reduce career stress. They introduce the 'life design compass' as a tool for navigation.

The authors guide identifying workview, lifeview, and playbook through reflective exercises.

They discuss reframing problems as design challenges, encouraging experimentation.

The chapter addresses fear of failure, promoting prototyping careers like informational interviews.

Burnett and Evans share stories of people who redesigned their lives for fulfillment.

They emphasize balance between curiosity and commitment.

The chapter concludes by empowering readers to build meaningful careers aligned with personal values.""",
     "K1",
     "Available"),

    ("peer-pressure",
     "The Art of Saying No",
     "Damon Zahariades",
     "Chapter 4: Overcoming Peer Pressure",
     """Chapter 4 of 'The Art of Saying No' by Damon Zahariades provides strategies for resisting peer pressure. Zahariades explains psychological mechanisms behind conformity.

He teaches assertive communication, like polite refusals without explanation.

The chapter discusses building self-awareness to recognize pressure triggers.

Zahariades shares techniques for setting boundaries and valuing personal integrity.

Case studies illustrate benefits of independence.

He concludes by affirming that saying no leads to authentic, stress-free living.""",
     "L2",
     "Available"),

    ("relationship",
     "The 5 Love Languages",
     "Gary Chapman",
     "Chapter 1: What Happens to Love After the Wedding?",
     """Chapter 1 of 'The 5 Love Languages' by Gary Chapman explores how love evolves post-marriage. Chapman identifies five languages: words of affirmation, acts of service, receiving gifts, quality time, and physical touch.

He explains misunderstandings when partners speak different languages, leading to stress.

The chapter provides examples of mismatched expressions causing hurt.

Chapman encourages discovering and speaking each other's language.

He shares stories of transformed relationships through this awareness.

The chapter concludes by promoting intentional love to maintain connection.""",
     "M1",
     "Available"),

    ("self-esteem",
     "The Self-Esteem Workbook",
     "Glenn R. Schiraldi",
     "Chapter 2: Building Self-Esteem",
     """Chapter 2 of 'The Self-Esteem Workbook' by Glenn R. Schiraldi offers exercises to boost self-esteem. Schiraldi defines self-esteem as self-acceptance and competence.

He guides identifying negative self-beliefs through journaling.

The chapter includes affirmations and visualization for positive change.

Schiraldi discusses unconditional self-acceptance versus performance-based esteem.

Exercises like self-compassion meditations are provided.

He shares research on self-esteem's impact on mental health.

The chapter concludes by encouraging consistent practice for lasting improvement.""",
     "N1",
     "Available"),

    ("time-management",
     "Getting Things Done",
     "David Allen",
     "Chapter 1: A New Practice for a New Reality",
     """Chapter 1 of 'Getting Things Done' by David Allen introduces the GTD method for stress-free productivity. Allen explains modern life's overwhelming inputs requiring a system.

He outlines capturing all tasks in an external system to clear the mind.

The chapter details processing items into actions, projects, or references.

Allen emphasizes weekly reviews for maintenance.

He shares benefits like reduced anxiety from open loops.

The chapter concludes by inviting adoption of GTD for control and focus.""",
     "O1",
     "Available"),

    ("self-doubt",
     "The War of Art",
     "Steven Pressfield",
     "Chapter 1: Resistance",
     """Chapter 1 of 'The War of Art' by Steven Pressfield identifies resistance as the enemy of creativity. Pressfield defines resistance as the force opposing meaningful work.

He explains resistance's manifestations like procrastination and self-sabotage.

The chapter discusses overcoming resistance through discipline and professionalism.

Pressfield shares personal and historical examples of conquered resistance.

He concludes by urging turning pro to achieve success.""",
     "P1",
     "Available"),

    ("time-management",
     "Eat That Frog",
     "Brian Tracy",
     "Chapter 2: Plan Every Day in Advance",
     """Chapter 2 of 'Eat That Frog' by Brian Tracy stresses planning for productivity. Tracy advocates starting the day with the most important task.

He explains benefits of planning in reducing stress and increasing efficiency.

The chapter provides tools like to-do lists and prioritization.

Tracy shares success stories from planning.

He concludes by encouraging daily planning for achievement.""",
     "Q1",
     "Available"),


    ("general",
     "Atomic Habits",
     "James Clear",
     "Chapter 1: Tiny Changes",
     """Chapter 1 of 'Atomic Habits' by James Clear explores how small, incremental changes can lead to remarkable transformations, reducing stress through sustainable habit formation. Clear begins by debunking the myth that major life changes require massive effort, instead emphasizing the power of 1% improvements that compound over time.

He introduces the concept of habit stacking, where new habits are built upon existing routines to make them easier to adopt. Clear explains the four stages of habit formation: cue (the trigger), craving (the motivation), response (the action), and reward (the satisfaction). Understanding this loop helps individuals break bad habits that contribute to stress and build positive ones that promote well-being.

The chapter discusses the importance of habit environment, showing how small changes in surroundings can make good habits more attractive and bad ones harder. Clear shares the story of the British cycling team, illustrating how marginal gains in training and nutrition led to Olympic success.

He addresses the plateau of latent potential, where early efforts seem fruitless but eventually lead to breakthroughs. This perspective helps reduce frustration and stress during personal growth journeys.

Clear provides practical strategies like habit tracking and accountability to maintain momentum. He concludes that by focusing on systems rather than goals, individuals can create lasting change that reduces stress and improves overall life satisfaction. This chapter empowers readers to take control of their habits for better mental health and productivity.""",
     "F1",
     "Available")
]

# Assign priorities to books (lower number = higher priority)
# We'll add priority to each book tuple
books_with_priority = []
for i, book in enumerate(books):
    # First 3 books get priority 1 (highest), rest get higher numbers
    priority = 1 if i < 3 else (2 if i < 6 else 3)
    books_with_priority.append(book + (priority,))

cursor.executemany("""
INSERT INTO books (stress_type, title, author, chapter, content, shelf, availability, priority)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", books_with_priority)

conn.commit()
conn.close()

print("Database created successfully!")
