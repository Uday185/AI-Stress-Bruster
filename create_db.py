# -*- coding: utf-8 -*-
"""
Database creation and initialization for MindEase
Populates library.db with philosophical and ethical books for stress relief
"""

import sqlite3
import os

# Database file
DB_FILE = "library.db"

# Comprehensive book database with philosophical and ethical books
BOOKS_DATA = {
    "academic": [
        {
            "title": "The Art of Learning",
            "author": "Josh Waitzkin",
            "chapter": "Chapter 1: Foundation",
            "content": "Master the art of learning by developing a growth mindset. This book teaches how to approach challenges as opportunities.",
            "shelf": "Self-Help",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Deep Work",
            "author": "Cal Newport",
            "chapter": "Introduction",
            "content": "In a world of distraction, learn how to focus deeply on meaningful intellectual work. Essential for academic success.",
            "shelf": "Productivity",
            "availability": "Available",
            "priority": 2
        },
        {
            "title": "Mindfulness for Beginners",
            "author": "Jon Kabat-Zinn",
            "chapter": "Chapter 2: Finding Your Center",
            "content": "Reduce exam anxiety through mindfulness meditation. Proven techniques to calm the mind during stressful periods.",
            "shelf": "Meditation",
            "availability": "Available",
            "priority": 1
        },
    ],

    "anxiety": [
        {
            "title": "The Upward Spiral",
            "author": "Alex Korb",
            "chapter": "Chapter 1: Neuroscience of Anxiety",
            "content": "Understand how your brain creates anxiety and practical ways to break the cycle through neuroscience-backed methods.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Feel the Fear and Do It Anyway",
            "author": "Susan Jeffers",
            "chapter": "The Root of Fear",
            "content": "Transform your relationship with fear and anxiety. Learn powerful techniques to move forward despite uncertainty.",
            "shelf": "Self-Help",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Emotional Agility",
            "author": "Susan David",
            "chapter": "Chapter 2: Thoughts as Passengers",
            "content": "Master your emotions and thoughts. Learn to respond rather than react to anxiety-inducing situations.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 2
        },
    ],

    "emotional": [
        {
            "title": "Man's Search for Meaning",
            "author": "Viktor Frankl",
            "chapter": "The Last of the Three Freedoms",
            "content": "A profound exploration of purpose and meaning in the face of suffering. A philosophical guide to emotional resilience.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Consolations of Philosophy",
            "author": "Alain de Botton",
            "chapter": "On Suffering",
            "content": "Ancient philosophical wisdom to navigate modern emotional pain. Practical comfort from great thinkers.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Emotional Intelligence",
            "author": "Daniel Goleman",
            "chapter": "Managing Emotion",
            "content": "Understand and master your emotions. Essential skills for emotional healing and growth.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 2
        },
    ],

    "career": [
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "chapter": "Chapter 1: The Compound Effect",
            "content": "Build career success through small, consistent habits. Transform your professional life one day at a time.",
            "shelf": "Career",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Ethics of Excellence",
            "author": "Aristotle (adapted by modern scholars)",
            "chapter": "Virtue in Work",
            "content": "Discover ethical excellence in your career. Build meaningful work aligned with your values.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Mindfulness at Work",
            "author": "David Gelles",
            "chapter": "Chapter 3: Performance",
            "content": "Reduce work stress through mindfulness. Improve focus, creativity, and job satisfaction.",
            "shelf": "Wellness",
            "availability": "Available",
            "priority": 2
        },
    ],

    "financial": [
        {
            "title": "The Simple Path to Wealth",
            "author": "JL Collins",
            "chapter": "Chapter 1: Understand Money",
            "content": "A philosophical approach to money and financial independence. Reduce stress through financial wisdom.",
            "shelf": "Finance",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Your Money or Your Life",
            "author": "Joe Dominguez & Vicki Robin",
            "chapter": "Chapter 1: The Money Game",
            "content": "Transform your relationship with money and financial stress. Ethical and practical financial guidance.",
            "shelf": "Finance",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Stoicism: Finding Inner Peace",
            "author": "William B. Irvine",
            "chapter": "On Financial Hardship",
            "content": "Stoic philosophy applied to financial challenges. Build inner strength independent of circumstances.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "family": [
        {
            "title": "Nonviolent Communication",
            "author": "Marshall B. Rosenberg",
            "chapter": "Chapter 2: Family Dynamics",
            "content": "Revolutionary approach to family conflict. Learn ethical communication that heals relationships.",
            "shelf": "Relationships",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Emotional Intelligence in the Family",
            "author": "Daniel Goleman",
            "chapter": "Family Bonds",
            "content": "Build stronger family relationships through emotional awareness and ethical communication.",
            "shelf": "Family",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Ethics of Care",
            "author": "Nel Noddings",
            "chapter": "Chapter 3: Family Care",
            "content": "Philosophical exploration of family relationships and ethical caring. Build compassionate family bonds.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "confidence": [
        {
            "title": "Daring Greatly",
            "author": "Brene Brown",
            "chapter": "Chapter 1: Wholehearted Living",
            "content": "Transform shame and vulnerability into confidence and courage. Authentic self-development.",
            "shelf": "Self-Help",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Mindset: The New Psychology of Success",
            "author": "Carol S. Dweck",
            "chapter": "Chapter 1: The Two Mindsets",
            "content": "Build confidence through a growth mindset. Scientific approach to self-belief.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Courage to Be",
            "author": "Paul Tillich",
            "chapter": "Existential Courage",
            "content": "Deep philosophical exploration of courage and authenticity. Find true confidence within.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "social": [
        {
            "title": "How to Win Friends and Influence People",
            "author": "Dale Carnegie",
            "chapter": "Chapter 3: Fundamental Techniques",
            "content": "Proven techniques for building genuine social connections and confidence in social situations.",
            "shelf": "Social Skills",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Gifts of Imperfection",
            "author": "Brene Brown",
            "chapter": "Chapter 2: Authenticity",
            "content": "Build authentic social connections by embracing your true self. Overcome social anxiety through authenticity.",
            "shelf": "Self-Help",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Friendship: A History",
            "author": "Alexander McCall Smith",
            "chapter": "Chapter 1: What Friendship Means",
            "content": "Philosophical exploration of genuine friendship and social connection. Build meaningful relationships.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "loneliness": [
        {
            "title": "Connection",
            "author": "Tara Marshall",
            "chapter": "Chapter 1: Understanding Loneliness",
            "content": "Scientific understanding of loneliness and practical ways to build meaningful connections.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Bowling Alone",
            "author": "Robert Putnam",
            "chapter": "Chapter 2: Community and Connection",
            "content": "Understand modern loneliness and discover ways to rebuild social fabric and community.",
            "shelf": "Sociology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Art of Solitude",
            "author": "Stephen Dunn",
            "chapter": "Solitude vs Loneliness",
            "content": "Philosophical distinction between loneliness and solitude. Transform isolation into meaningful introspection.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "breakup": [
        {
            "title": "The New Rules of Divorce",
            "author": "Jacqueline Newman",
            "chapter": "Chapter 1: Emotional Healing",
            "content": "Navigate heartbreak with wisdom. Practical and emotional guidance through relationship loss.",
            "shelf": "Relationships",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Attached: The New Science of Adult Attachment",
            "author": "Amir Levine & Rachel Heller",
            "chapter": "Chapter 7: Healing",
            "content": "Understand attachment patterns and heal from breakups. Build healthier future relationships.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Sovereignty of Love",
            "author": "bell hooks",
            "chapter": "Chapter 3: Healing and Wholeness",
            "content": "Philosophical and spiritual approach to healing from heartbreak. Love, healing, and personal growth.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "health": [
        {
            "title": "When Breath Becomes Air",
            "author": "Paul Kalanithi",
            "chapter": "Chapter 1: Facing Mortality",
            "content": "Profound meditation on health, mortality, and living meaningfully. A transformative read.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Healing Mind",
            "author": "Paul D. Nussbaum",
            "chapter": "Chapter 2: Mind-Body Connection",
            "content": "Understand the mind-body connection in healing. Take active role in health recovery.",
            "shelf": "Health",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Full Medical Catastrophe",
            "author": "Jon Kabat-Zinn",
            "chapter": "Chapter 3: Healing",
            "content": "Mindfulness-based approach to health stress. Scientific study of healing through awareness.",
            "shelf": "Wellness",
            "availability": "Available",
            "priority": 2
        },
    ],

    "peer-pressure": [
        {
            "title": "The Courage to Stand Alone",
            "author": "William Ury",
            "chapter": "Chapter 1: Finding Your Voice",
            "content": "Develop courage to resist peer pressure. Stand authentic despite external influence.",
            "shelf": "Self-Help",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Your Tribe Determines Your Vibe",
            "author": "Trouper Reid",
            "chapter": "Chapter 2: Choosing Your People",
            "content": "Learn to choose communities aligned with your values. Overcome negative peer influence.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Ethics and Authenticity",
            "author": "Charles Taylor",
            "chapter": "Chapter 1: Being True to Yourself",
            "content": "Deep philosophical exploration of authenticity and ethical living despite social pressure.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "relationship": [
        {
            "title": "Mating in Captivity",
            "author": "Esther Perel",
            "chapter": "Chapter 1: Sustaining Desire",
            "content": "Navigate relationship challenges with wisdom. Build stronger, more authentic partnerships.",
            "shelf": "Relationships",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Relationship Cure",
            "author": "John Gottman",
            "chapter": "Chapter 2: Repair Attempts",
            "content": "Evidence-based strategies to improve relationships. Ethical communication and conflict resolution.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Symposium (Modern Edition)",
            "author": "Plato",
            "chapter": "On Love",
            "content": "Ancient philosophical exploration of love and relationships. Timeless wisdom on partnership.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "self-esteem": [
        {
            "title": "The Six Pillars of Self-Esteem",
            "author": "Nathaniel Branden",
            "chapter": "Chapter 1: Understanding Self-Esteem",
            "content": "Comprehensive guide to building genuine self-worth. Move beyond shallow confidence.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Self-Compassion",
            "author": "Kristin Neff",
            "chapter": "Chapter 2: Self-Kindness",
            "content": "Build self-esteem through self-compassion rather than self-criticism. Scientifically proven approach.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Being and Nothingness",
            "author": "Jean-Paul Sartre",
            "chapter": "Chapter 3: Authenticity",
            "content": "Existential philosophy of authentic self and freedom. Philosophical foundation for true self-esteem.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "time-management": [
        {
            "title": "Essentialism",
            "author": "Greg McKeown",
            "chapter": "Chapter 1: The Way of the Essentialist",
            "content": "Learn to focus on what truly matters. Strategic approach to time and priorities.",
            "shelf": "Productivity",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Four Thousand Weeks",
            "author": "Oliver Burkeman",
            "chapter": "Introduction: The Infinity Paradox",
            "content": "Philosophical approach to time management. Accept mortality and live more meaningfully.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Getting Things Done",
            "author": "David Allen",
            "chapter": "Chapter 2: Capturing",
            "content": "Practical system to manage tasks and stress. Organized approach to productivity.",
            "shelf": "Productivity",
            "availability": "Available",
            "priority": 2
        },
    ],

    "self-doubt": [
        {
            "title": "The Secret Thoughts of Successful Women",
            "author": "Valerie Young",
            "chapter": "Chapter 1: Imposter Syndrome",
            "content": "Overcome imposter syndrome and self-doubt. Build authentic confidence.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Mindset",
            "author": "Carol S. Dweck",
            "chapter": "Chapter 3: Sports, Music, and Self-esteem",
            "content": "Transform self-doubt through growth mindset. Scientifically backed approach to capability.",
            "shelf": "Psychology",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Myth of Sisyphus",
            "author": "Albert Camus",
            "chapter": "Absurdism and Self-Worth",
            "content": "Deep philosophical exploration of meaning and self-worth despite uncertainty.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ],

    "general": [
        {
            "title": "The Stoic Way of Life",
            "author": "William B. Irvine",
            "chapter": "Chapter 1: Stoic Principles",
            "content": "Universal wisdom from Stoic philosophy. Practical techniques for peace and resilience.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "Meditations",
            "author": "Marcus Aurelius",
            "chapter": "Book 1: On Duty",
            "content": "Ancient wisdom from a Stoic emperor. Universal guide to finding peace and purpose.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 1
        },
        {
            "title": "The Courage to Be Disliked",
            "author": "Ichiro Kishimi & Fumitake Koga",
            "chapter": "Chapter 1: Meeting",
            "content": "Adlerian psychology mixed with Buddhism. Find freedom and happiness through ethical living.",
            "shelf": "Philosophy",
            "availability": "Available",
            "priority": 2
        },
    ]
}


def generate_chapter_summary(title, author, chapter, content, stress_type):
    """Generate essay-style summaries tailored to each stress type."""

    summaries = {
        "academic": chapter + " from '" + title + "' by " + author + " explores the intersection of learning and stress management. In our modern educational landscape, academic pressure often stems from perfectionism and the fear of failure rather than the material itself. This chapter illuminates how successful learners reframe challenges as opportunities for growth rather than threats to self-worth. By understanding the psychology of learning, you'll discover that stress diminishes when you focus on progress instead of perfection. The author shares evidence-based techniques for maintaining focus during intense study sessions, managing exam anxiety through structured preparation, and building a growth mindset that transforms setbacks into learning moments. The practical framework presented here helps you develop resilience not just for exams, but for lifelong learning. Throughout this journey, you'll learn that your capacity to adapt and improve is far greater than any single grade or test score. The chapter concludes with actionable steps to create a personalized study environment that supports both academic excellence and emotional well-being.",

        "anxiety": chapter + " from '" + title + "' by " + author + " delves into the neuroscience and psychology of anxiety, offering a compassionate understanding of this universal experience. Anxiety is not a flaw or weakness - it's your nervous system's attempt to protect you, albeit sometimes overprotectively. This chapter breaks down how anxiety develops in the brain and body, helping you recognize the difference between productive worry and rumination that fuels distress. The author presents scientifically validated techniques for interrupting the anxiety cycle, including breathwork, grounding practices, and cognitive strategies that reduce the power anxiety holds over your life. You'll learn how small, consistent actions gradually retrain your nervous system to feel safer in situations that previously triggered panic. What makes this chapter particularly valuable is its emphasis on self-compassion rather than fighting against your anxiety. By accepting anxiety as a natural part of the human experience, you paradoxically reduce its grip on your daily life. The practical exercises provided can be implemented immediately, offering tangible relief and long-term resilience.",

        "emotional": chapter + " from '" + title + "' by " + author + " offers profound philosophical and psychological wisdom for navigating emotional pain and grief. Emotional struggles often arise not from feeling too much, but from judging ourselves for what we feel or suppressing emotions entirely. This chapter explores the nature of suffering and meaning, drawing on both modern psychology and ancient philosophy to show how emotional pain can become a source of growth and deeper understanding. The author guides you through the process of honoring your emotions - whether sadness, anger, or despair - while maintaining hope and perspective. Throughout these pages, you'll discover that resilience does not mean avoiding pain, but rather developing a compassionate relationship with your emotional landscape. The chapter includes reflective practices that help you process difficult feelings and extract wisdom from your struggles. By the end, you'll understand that emotional depth and vulnerability are not weaknesses but gateways to authentic living and meaningful connection with others. This transformative perspective can fundamentally shift how you experience and move through emotional challenges.",

        "career": chapter + " from '" + title + "' by " + author + " addresses the challenge of building a meaningful career while managing professional stress and self-doubt. Career stress often stems from the gap between your current reality and your aspirations, complicated by workplace dynamics and performance pressure. This chapter presents a philosophy of gradual growth and continuous improvement that reduces the burden of having to be perfect immediately. You'll learn how small, consistent habits compound over time to create significant professional advancement and satisfaction. The author emphasizes the importance of aligning your work with your values and strengths, discovering that career fulfillment comes not from climbing a predetermined ladder but from crafting work that matters to you. The chapter provides practical strategies for managing workplace relationships, handling criticism constructively, and maintaining boundaries that protect your well-being. Throughout this exploration, you'll recognize that sustainable career success is built on resilience, continuous learning, and genuine effort rather than overnight breakthroughs. These insights help you approach your career with both ambition and compassion for yourself.",

        "financial": chapter + " from '" + title + "' by " + author + " offers a refreshing, humanistic perspective on money and financial stress. Financial anxiety often emerges not from lacking resources but from viewing money through a lens of fear and scarcity. This chapter shifts your relationship with finances from one of anxiety to one of intentionality and agency. The author explores how financial stress impacts overall well-being and presents evidence-based approaches to building financial stability without obsession. You'll discover that financial health is less about earning a certain amount and more about aligning your spending with your values and creating sustainable habits. The chapter demystifies personal finance, replacing jargon and complexity with clear, actionable principles anyone can implement. Importantly, it addresses the emotional dimensions of money - shame, fear, envy - that often undermine financial decision-making more than any math ever could. By reframing financial management as a form of self-respect and care, this chapter helps you take control of your finances in a way that feels empowering rather than restrictive. The result is both practical financial progress and genuine peace of mind.",

        "family": chapter + " from '" + title + "' by " + author + " explores the complexity of family relationships and the communication patterns that either heal or harm family bonds. Family stress frequently arises from unmet expectations, unresolved conflicts, and communication breakdowns passed through generations. This chapter presents a compassionate framework for understanding family dynamics while offering concrete tools for healthier interaction. The author teaches how nonviolent, empathetic communication can transform even deeply entrenched family conflicts, helping family members feel heard and respected despite disagreements. You'll learn to identify triggers, understand different perspectives, and respond to family challenges with both strength and tenderness. The chapter acknowledges that family relationships are often complicated - mixing love with frustration, loyalty with resentment - and that's entirely normal and workable. Through reflective exercises and practical dialogue techniques, you'll develop the skills to maintain your emotional integrity while strengthening family connections. This approach recognizes that healing family relationships is a gradual process, but one that yields tremendous rewards for your own well-being and sense of belonging.",

        "confidence": chapter + " from '" + title + "' by " + author + " challenges the myth that confidence is something you either have or don't, presenting instead a practical path to building authentic self-belief. True confidence does not come from being fearless or perfect - it emerges from taking action despite uncertainty and honoring your authentic self. This chapter guides you through understanding the roots of self-doubt and gradually expanding your comfort zone through small, courageous acts. The author explains how competence builds confidence through repeated experience and reflection, creating an upward spiral where small successes compound into genuine self-belief. You'll discover that vulnerability and authenticity are actually the foundations of real confidence, not signs of weakness. The chapter includes vulnerable storytelling and research that normalizes self-doubt, showing you're not alone in these feelings. Most importantly, you'll learn that confidence is a skill you can develop through deliberate practice, self-compassion, and consistent alignment with your values. By the end of this chapter, you'll have a personal roadmap for building the kind of deep, resilient confidence that comes from knowing yourself and trusting your capacity to navigate life's challenges.",

        "social": chapter + " from '" + title + "' by " + author + " addresses the universal human need for connection while acknowledging that social interaction can feel overwhelming for many. Social stress often comes not from lacking social skills but from anxiety about judgment and fear of rejection. This chapter reframes social interaction as a learnable skill rather than an innate talent, offering specific, practical techniques for building genuine connections. The author explores the psychology of authentic conversation, showing how small acts of genuine interest and curiosity naturally attract others and deepen relationships. You'll discover that most people share your social anxieties and appreciate your efforts to connect, even if those efforts feel awkward to you. The chapter provides concrete approaches for starting conversations, managing social anxiety, and finding your people - the communities and individuals who appreciate your authentic self. Throughout these pages, you'll learn that social courage does not mean being the loudest or most outgoing person in the room, but rather showing up authentically despite your nervousness. The practical strategies here can gradually transform your relationship with social situations from dreaded to genuinely enjoyable.",

        "loneliness": chapter + " from '" + title + "' by " + author + " makes an important distinction between loneliness and solitude while offering pathways to meaningful connection. Loneliness is not simply about being alone - it's about the pain of disconnection when connection is desired. This chapter explores how modern life can increase feelings of isolation despite constant connectivity, and what genuine connection actually requires. The author presents research showing that deep relationships are built on vulnerability, consistency, and mutual care rather than large friend groups or social media presence. You'll learn practical strategies for initiating and nurturing meaningful relationships, overcoming the shame often associated with loneliness, and recognizing that reaching out for connection is a sign of strength. The chapter acknowledges that building community takes time and repeated effort, but the investment yields tremendous returns for your mental health and sense of belonging. Importantly, the author teaches how to distinguish between healthy solitude - necessary for reflection and recharging - and painful isolation. By the end of this chapter, you'll have both the motivation and practical tools to gradually weave genuine human connection back into your life.",

        "breakup": chapter + " from '" + title + "' by " + author + " compassionately guides you through the unique pain of romantic loss and heartbreak. Breakups often hurt not just because of the loss of a relationship, but because they can shake your sense of identity and self-worth. This chapter normalizes the full range of emotions that accompany heartbreak - grief, anger, confusion, even moments of relief - while providing a framework for moving through rather than getting stuck in this pain. The author explores attachment patterns and relationship dynamics with gentleness, helping you understand what happened without harsh self-judgment. You'll learn that healing from heartbreak is not about forgetting the relationship or denying its significance, but about integrating this experience into your life story in a way that fosters growth. The chapter provides practical guidance for managing daily life during acute heartbreak, rebuilding your identity as a single person, and gradually rebuilding your capacity to trust and connect. Throughout this exploration, you'll discover that heartbreak, while profoundly painful, contains seeds of self-discovery and personal development. The result is not just healing, but a deeper, more compassionate understanding of yourself and what you want from relationships.",

        "health": chapter + " from '" + title + "' by " + author + " examines the profound connection between mind and body in health and healing. Health challenges often carry emotional weight alongside physical symptoms - fear, grief, identity disruption, and loss of control. This chapter integrates physical and psychological approaches to health stress, showing how stress and negative emotions can impair healing while hope and peace support it. The author explores how taking an active role in your health - through lifestyle choices, medical decision-making, and psychological resilience - can significantly impact outcomes and well-being. You'll discover that this is not about positive thinking solving physical problems, but rather about recognizing genuine connections between your mental state and physical health. The chapter provides practical techniques for managing health anxiety, communicating effectively with healthcare providers, and building trust in your body's capacity to heal and adapt. Throughout these pages, you'll learn that facing health challenges with knowledge, agency, and self-compassion yields better outcomes than fear and helplessness. By the end, you'll understand that your role in your own healing is far more significant than most people realize, and this recognition itself becomes a source of hope and empowerment.",

        "peer-pressure": chapter + " from '" + title + "' by " + author + " explores the deep human need to belong while asserting that true belonging requires remaining true to yourself. Peer pressure is not just a teenage phenomenon - it affects us throughout life as we navigate social expectations and the fear of rejection. This chapter distinguishes between healthy adaptation to communities and harmful compromise of your values and authenticity. The author presents the psychology of conformity and influence, helping you understand why peer pressure feels so compelling and how to maintain your integrity within it. You'll learn that the people and communities worth staying connected to actually appreciate your authenticity rather than punishing it. The chapter offers practical strategies for asserting your values respectfully, finding supportive communities aligned with who you are, and managing the temporary discomfort of standing apart from the crowd. Throughout this exploration, you'll discover that your authentic self is your greatest asset, not a liability to manage or hide. By the end, you'll have both the insight and practical tools to navigate social pressure while remaining true to yourself and your values.",

        "relationship": chapter + " from '" + title + "' by " + author + " delves into the complexity of romantic partnerships, acknowledging both their challenges and their profound potential for growth and happiness. Relationship stress often emerges from unmet expectations, communication breakdowns, and the clash between different attachment styles and needs. This chapter presents a mature perspective on partnership that moves beyond romantic myths toward realistic, compassionate understanding of how relationships develop and thrive. The author explores how partners can maintain individual identity while building genuine intimacy, manage conflict constructively, and continually deepen connection. You'll learn that healthy relationships require ongoing communication, flexibility, and the ability to repair conflicts rather than avoid them. The chapter includes frameworks for understanding your partner's perspective, expressing your needs clearly, and building trust through consistency and vulnerability. Throughout these pages, you'll discover that relationship challenges often contain opportunities for growth for both partners and for the relationship itself. By the end, you'll have practical wisdom for building a partnership characterized by genuine understanding, authentic support, and the kind of love that strengthens rather than diminishes who you are.",

        "self-esteem": chapter + " from '" + title + "' by " + author + " offers a profound exploration of genuine self-worth and how to build it on stable ground. Self-esteem issues often stem not from high standards but from self-criticism, comparison, and conditional self-worth based on external achievements. This chapter distinguishes between shallow confidence and genuine self-respect, showing how the latter comes from living in alignment with your values and treating yourself with kindness. The author explores how childhood experiences, societal messages, and life events have shaped your current self-perception, and how you can gently reshape those beliefs through awareness and new experiences. You'll learn that self-esteem is built through small acts of self-compassion, setting healthy boundaries, pursuing meaningful goals, and developing genuine competence. The chapter normalizes imperfection, showing that self-worth does not require being perfect but rather accepting yourself fully while still growing and improving. Throughout this exploration, you'll discover that the quality of your self-esteem depends less on external accomplishment and more on internal dialogue and self-relationship. By the end, you'll have both the understanding and practical tools to build a foundation of genuine, resilient self-worth that weathers life's inevitable challenges.",

        "time-management": chapter + " from '" + title + "' by " + author + " reframes time management not as a productivity hack but as an expression of your values and priorities. Time stress often comes from trying to do too much, from unclear priorities, and from the constant pressure of modern life. This chapter presents a philosophical perspective on time - acknowledging its finite nature - that paradoxically reduces time anxiety while increasing meaningful productivity. The author helps you identify what truly matters to you, then shows how to align your time allocation with these priorities. You'll discover that effective time management is less about rigid schedules and more about clear values, regular reflection, and the courage to say no to good opportunities in order to say yes to what's best. The chapter provides practical systems for capturing tasks, planning realistically, and protecting your energy and attention from constant demands. Throughout these pages, you'll learn that the goal is not to accomplish everything possible but to accomplish what genuinely matters to you. By the end, you'll have replaced anxiety-driven busyness with intentional focus on your real priorities, resulting in both greater accomplishment and deeper peace of mind.",

        "self-doubt": chapter + " from '" + title + "' by " + author + " addresses imposter syndrome and self-doubt with both compassion and practical wisdom. Self-doubt often comes from comparing yourself to others' highlights, internalizing others' doubts, or holding yourself to impossible standards. This chapter normalizes self-doubt as a nearly universal experience among capable people while showing how to manage it so it does not paralyze you. The author explores the psychology of self-doubt and imposter syndrome, showing that these feelings often say more about your standards and sensitivity than about your actual capabilities. You'll learn that evidence of your competence is all around you - in past accomplishments, positive feedback, and successful navigation of challenges - but self-doubt can make this evidence invisible. The chapter provides techniques for recognizing and challenging self-critical thoughts, building evidence of your capabilities through deliberate reflection, and taking action despite doubt. Throughout this exploration, you'll discover that self-doubt diminishes not through achieving more external validation but through internal practices of self-compassion and realistic self-assessment. By the end, you'll understand that self-doubt and competence can coexist, and that acting despite doubt is the path to genuine confidence.",

        "general": chapter + " from '" + title + "' by " + author + " offers universal wisdom for navigating life's inevitable stresses and challenges with resilience and grace. Stress, in its many forms, is a natural part of human experience - it's not something to eliminate but rather something to understand and manage wisely. This chapter draws on timeless philosophical traditions and modern psychology to present an integrated approach to stress that addresses both practical challenges and deeper meaning-making. The author helps you develop resilience not through forcing yourself to be tough but through understanding your values, building supportive relationships, and developing self-compassion in the face of difficulty. You'll learn that stress often signals that something in your life needs attention - whether it's unrealistic expectations, unmet needs, or misalignment with your values. The chapter provides practical strategies for managing immediate stress while also addressing root causes. Throughout these pages, you'll discover that your capacity to overcome challenges is greater than you realize, and that adversity often contains opportunities for growth and wisdom. By the end, you'll have both the mindset and practical tools to navigate whatever life brings with increasing courage, clarity, and compassion for yourself.",
    }

    return summaries.get(stress_type, summaries["general"])


def create_database():
    """Create the library database and populate it with books."""

    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print("[*] Removed old " + DB_FILE)

    # Connect to database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create books table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stress_type TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            chapter TEXT NOT NULL,
            content TEXT NOT NULL,
            chapter_summary TEXT NOT NULL,
            shelf TEXT NOT NULL,
            availability TEXT NOT NULL,
            priority INTEGER
        )
    """)

    total_books = 0
    for stress_type, books in BOOKS_DATA.items():
        for book in books:
            chapter_summary = generate_chapter_summary(
                title=book["title"],
                author=book["author"],
                chapter=book["chapter"],
                content=book["content"],
                stress_type=stress_type,
            )
            cursor.execute(
                """
                INSERT INTO books
                (stress_type, title, author, chapter, content, chapter_summary, shelf, availability, priority)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    stress_type,
                    book["title"],
                    book["author"],
                    book["chapter"],
                    book["content"],
                    chapter_summary,
                    book["shelf"],
                    book["availability"],
                    book["priority"],
                ),
            )
            total_books += 1

    # Commit and close
    conn.commit()
    conn.close()

    print("[OK] Database created successfully!")
    print("[*] Total books added: " + str(total_books))
    print("[*] Stress categories: " + str(len(BOOKS_DATA)))
    for stress_type in sorted(BOOKS_DATA.keys()):
        print("   - " + stress_type + ": " + str(len(BOOKS_DATA[stress_type])) + " books")


def verify_database():
    """Verify the database was created correctly."""
    if not os.path.exists(DB_FILE):
        print("[FAIL] Database file not found: " + DB_FILE)
        return False

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Count books
        cursor.execute("SELECT COUNT(*) FROM books")
        total = cursor.fetchone()[0]

        # Count by stress type
        cursor.execute("SELECT stress_type, COUNT(*) FROM books GROUP BY stress_type ORDER BY stress_type")
        results = cursor.fetchall()

        print("\n[*] Database Verification:")
        print("[OK] Total books: " + str(total))
        print("[OK] Stress categories:")
        for stress_type, count in results:
            print("   - " + stress_type + ": " + str(count) + " books")

        conn.close()
        return True
    except Exception as e:
        print("[FAIL] Error verifying database: " + str(e))
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("[BUILD] Building MindEase Library Database")
    print("=" * 60)
    create_database()
    print()
    verify_database()
    print("\n[DONE] Database setup complete!")
