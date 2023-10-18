import ai21
import streamlit as st

ai21.api_key = '3jKXNgXeY7qa6wdIFIr5hcwglABeqrzC'
#ai21.api_key = st.secrets['api-keys']['ai21-algo-team-prod']

DEFAULT_MODEL = 'j2-ultra'

SUMMARIZATION_URL = "https://www.ai21.com/blog/announcing-ai21-studio-and-jurassic-1"
SUMMARIZATION_TEXT = '''Perhaps no other crisis in modern history has had as great an impact on daily human existence as COVID-19. And none has forced businesses throughout the world to accelerate their evolution as their leaders worked to respond and recover on the way to thriving in the postpandemic environment.

Deloitte Private’s latest global survey of private enterprises reveals that executives in every region used the crisis as a catalyst, accelerating change in virtually all aspects of how we work and live. They stepped up their digital transformation through greater technology investment and deployment. In-progress initiatives were pushed toward completion, while those that were on the drawing board came to life. They sought out new partnerships and alliances. They pursued new opportunities to strengthen their supply networks and grow markets. They increased efforts to understand their purpose beyond profits, seeking new ways to grow sustainably and strengthen trust with their employees, customers, and other key stakeholders. They also embraced new possibilities in how and where work gets done.
'''

CLASSIFICATION_FEWSHOT="""Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
Astronomers Observe Collision of Galaxies, Formation of Larger
Summary:
An international team of astronomers has obtained the clearest images yet of the merger of two distant clusters of galaxies, calling it one of the most powerful cosmic events ever witnessed.
The topic of this article is:
Science and Technology

===

Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
Bomb Explodes Near U.S. Military Convoy (AP)
Summary:
AP - A car bomb exploded early Sunday near a U.S. military convoy on the road leading to Baghdad's airport, Iraqi police said, and a witness said two Humvees were destroyed.
The topic of this article is:
World

===

Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
Maradona goes to Cuba
Summary:
The former Argentine football star, Diego Armando Maradona, traveled on Monday to Cuba to continue his treatment against his addiction to drugs.
The topic of this article is:
Sports

===

Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology
Title:
Duke earnings jump in third quarter
Summary:
Duke Energy Corp. reports third-quarter net income of  $389 million, or 41 cents per diluted share, sharply above earnings of  $49 million, or 5 cents per diluted share, in the same period last year.
The topic of this article is:
Business

===

"""

CLASSIFICATION_PROMPT="""Classify the following news article into one of the following topics:
1. World
2. Sports
3. Business
4. Science and Technology"""

CLASSIFICATION_TITLE = "D.C. Unveils Stadium Plan"

CLASSIFICATION_DESCRIPTION = "Rumors spread that Major League Baseball is edging closer to moving the Expos to Washington as D.C. officials announce plans for a stadium on the Anacostia waterfront."

PRODUCT_DESCRIPTION_FEW_SHOT = '''Write product descriptions for fashion eCommerce site based on a list of features.
Product: On Every Spectrum Fit and Flare Dress
Features:
- Designed by Retrolicious
- Stretch cotton fabric
- Side pockets
- Rainbow stripes print
Description: In a bold rainbow-striped print, made up of exceptionally vibrant hues, this outstanding skater dress from Retroliciousis on every spectrum of vintage-inspired style. Made from a stretchy cotton fabric and boasting a round neckline, a sleeveless fitted bodice, and a gathered flare skirt with handy side pockets, this adorable fit-and-flare dress is truly unique and so retro-chic.

##

Write product descriptions for fashion eCommerce site based on a list of features.
Product: Camp Director Crossbody Bag
Features:
- Black canvas purse
- Rainbow space print
- Leather trim
- Two securely-zipped compartments
Description: Take a bit of camp charm with you wherever you go with this black canvas purse! Adorned with a rainbow space motif print, black faux-leather trim, two securely-zipped compartments, and adjustable crossbody strap, this ModCloth-exclusive bag makes sure you command a smile wherever you wander.

##

Write product descriptions for fashion eCommerce site based on a list of features.'''

WEBSITE_Email_Template_FEW_SHOT = '''Write an email marketing template for the following company.

Name of Business: Green Thumb Landscaping
Location: Portland, OR
Services:
- Landscape Design
- Lawn Maintenance
- Tree Pruning
- Irrigation Systems

Important Company Highlights:
- Eco-friendly practices
- Certified Arborists
- 100% Customer Satisfaction Guarantee

Email:
Subject: Unlock a Greener Tomorrow with Our Exclusive Landscaping Services!

Dear [Customer's First Name],
Welcome to Green Thumb Landscaping - where your garden dreams come to life!
Discover the beauty of top-tier Landscape Design as your space transforms before your eyes. Benefit from our meticulous 
Lawn Maintenance services and maintain a pristine lawn year-round. Trust in our Certified Arborists to give your trees 
the expert care they deserve with our Tree Pruning service. And with our efficient Irrigation Systems, your garden will always stay vibrant and lush.
More than that, our commitment to eco-friendly practices ensures a green and sustainable outcome for your outdoor spaces.
And with our 100% Customer Satisfaction Guarantee, we ensure your complete satisfaction.

Book now and embrace nature like never before!

Warm regards,
Green Thumb Landscaping Team, Portland, OR

##

Write an email marketing template for the following company.

Name of Business: Tech Genie IT Solutions
Location: Austin, TX
Services:
- IT Consulting
- Network Security
- Cloud Services
- Data Backup & Recovery

Important Company Highlights:
- 24/7 IT Support
- Certified Technicians
- Customized Solutions for Businesses

Email:
Subject: Elevate Your IT Experience with Tech Genie Solutions!

Hello [Customer's First Name],
Step into the future with Tech Genie IT Solutions!
Fortify your business framework with our cutting-edge Network Security services. Optimize and streamline with our Cloud 
Services. Never lose important data again with our Data Backup & Recovery solutions. And if you're unsure about the best
 IT strategies for your business, our Consulting services are here to guide you.
With certified technicians on standby 24/7, we're always here to support and ensure your operations run seamlessly.
And remember, each solution is customized to fit your unique business needs.

Ready to transform your IT landscape? Get in touch today!

Best wishes,
Tech Genie Team, Austin, TX

##

Write an email marketing template for the following company.

Name of Business: Fresh Bites Catering
Location: Chicago, IL
Services:
- Corporate Catering
- Event Planning
- Custom Menu Design
- Dietary Options

Company Highlights:
- Farm-to-table Ingredients
- Experienced Event Coordinators
- On-time Delivery

Email:
Subject: Make Every Occasion Memorable with Fresh Bites Catering!

Dear [Customer's First Name],
Introducing Fresh Bites Catering - your culinary solution for every occasion!
Choose our Corporate Catering services to impress at every corporate gathering. 
Allow our Experienced Event Coordinators to take the reins and make your events a resounding success. 
Personalize your guest experience with our Custom Menu Design. And with our wide range of Dietary Options,
everyone's palate will be catered to.
Our promise? Only the freshest, farm-to-table ingredients in every bite, delivered right on time.

Experience the Fresh Bites difference. Book your event today!

Best regards,
Fresh Bites Team, Chicago, IL

##

Write an email marketing template for the following company.

Name of Business: Artistic Ink Tattoo Studio 
Location: Seattle, WA
Services:
- Custom Tattoos
- Cover-ups
- Body Piercing
- Tattoo Removal

Important Company Highlights:
- Award-winning Artists
- Strict Sanitary Standards
- Free Consultations

Email:
Subject: Craft Your Story on Skin at Artistic Ink Tattoo Studio!

Hello [Customer's First Name],
Step into the world of Artistic Ink Tattoo Studio, where art meets passion.
Let our Award-winning Artists turn your vision into a lasting piece of art. Reimagine your past tattoos with our 
Cover-ups service. Elevate your style with our precision Body Piercing. And if you ever change your mind, our 
Tattoo Removal services are here to help.
Your safety and satisfaction are paramount. Our strict sanitary standards ensure you receive your tattoos in a 
clean and secure environment. And before you decide, we invite you for a free consultation to discuss your ideas.

Ready to craft your unique story? Visit us today!

Warm regards,
Artistic Ink Team, Seattle, WA

##

Write an email marketing template for the following company.

##

'''

WEBSITE_FAQ_FEW_SHOT = '''Write frequently asked questions (FAQ) for the following company.

Name of Business: Green Thumb Landscaping
Location: Portland, OR
Services:
- Landscape Design
- Lawn Maintenance
- Tree Pruning
- Irrigation Systems

Important Company Highlights:
- Eco-friendly practices
- Certified Arborists
- 100% Customer Satisfaction Guarantee

FAQ:
Q1: Do you use eco-friendly products and methods in your landscaping services?
A1: Absolutely! We take pride in our commitment to eco-friendly practices, ensuring that our landscapes are both beautiful and environmentally sustainable.

Q2: Are your arborists certified?
A2: Yes, we have certified arborists on our team, guaranteeing expert care for your trees during pruning and other services.

Q3: What if I'm not satisfied with the landscaping job?
A3: We offer a 100% Customer Satisfaction Guarantee. If you're not happy, we'll make it right.

##

Write frequently asked questions (FAQ) for the following company.

Name of Business: Tech Genie IT Solutions
Location: Austin, TX
Services:
- IT Consulting
- Network Security
- Cloud Services
- Data Backup & Recovery

Important Company Highlights:
- 24/7 IT Support
- Certified Technicians
- Customized Solutions for Businesses

FAQ:
Q1: Do you provide IT support round the clock?
A1: Yes, we offer 24/7 IT support to ensure your business operations run smoothly at all times.

Q2: Are your technicians certified?
A2: Absolutely! Our technicians are certified, ensuring top-notch services and solutions for your IT needs.

Q3: Can you provide a solution tailored for my specific business needs?
A3: Definitely. We specialize in crafting customized IT solutions that cater specifically to your business requirements.

##

Write frequently asked questions (FAQ) for the following company.

Name of Business: Fresh Bites Catering
Location: Chicago, IL
Services:
- Corporate Catering
- Event Planning
- Custom Menu Design
- Dietary Options

Company Highlights:
- Farm-to-table Ingredients
- Experienced Event Coordinators
- On-time Delivery

FAQ:
Q1: Do you use organic ingredients in your dishes?
A1: Yes, we prioritize farm-to-table ingredients, ensuring that our meals are fresh, organic, and of the highest quality.

Q2: Can you accommodate specific dietary restrictions?
A2: Absolutely! We offer various dietary options and can create a custom menu tailored to your needs.

Q3: What if my catering order is late?
A3: We pride ourselves on timely delivery. In the rare case of a delay, our team will communicate and ensure a swift resolution

##

Write frequently asked questions (FAQ) for the following company.

Name of Business: Artistic Ink Tattoo Studio 
Location: Seattle, WA
Services:
- Custom Tattoos
- Cover-ups
- Body Piercing
- Tattoo Removal

Important Company Highlights:
- Award-winning Artists
- Strict Sanitary Standards
- Free Consultations

FAQ:
Q1: Do you offer consultations before getting a tattoo?
A1: Yes, we provide free consultations to discuss design, placement, and any other queries you might have.

Q2: Are your tattoo artists certified or have won any awards?
A2: Absolutely! We boast award-winning artists who are passionate about crafting unique and intricate designs for our clients.

Q3: How do you ensure the hygiene of your studio?
A3: We maintain strict sanitary standards, ensuring all our equipment is sterilized and our studio is immaculately clean to guarantee the safety of our clients.

##

Write frequently asked questions (FAQ) for the following company.

##

'''

WEBSITE_TESTIMONIAL_FEW_SHOT = '''Write an engaging and promotional testimonials for the following company.

Name of Business: Green Thumb Landscaping
Location: Portland, OR
Services:
- Landscape Design
- Lawn Maintenance
- Tree Pruning
- Irrigation Systems

Important Company Highlights:
- Eco-friendly practices
- Certified Arborists
- 100% Customer Satisfaction Guarantee

Testimonial:
"I recently collaborated with Green Thumb Landscaping for my backyard redesign in Portland,
and the experience was outstanding! Their eco-friendly approach aligns perfectly with my values. 
The team, especially their certified arborists, 
took great care in tree pruning and setting up an effective irrigation system. Their dedication to 100% customer 
satisfaction is evident in every blade of grass. Highly recommend for anyone in need of landscaping services!"

##

Write an engaging and promotional testimonials for the following company.

Name of Business: Tech Genie IT Solutions
Location: Austin, TX
Services:
- IT Consulting
- Network Security
- Cloud Services
- Data Backup & Recovery

Important Company Highlights:
- 24/7 IT Support
- Certified Technicians
- Customized Solutions for Businesses

Testimonial:
"Our company has been partnered with Tech Genie IT Solutions for over a year, and they've been an IT lifesaver!
 The 24/7 support is a game-changer, especially during our late-night work sessions.
 With certified technicians who craft customized solutions, our network security has never been tighter.
 Data backup & recovery was seamless when we had an unexpected system failure.
 Tech Genie is truly the guardian of our IT infrastructure in Austin."

##

Write an engaging and promotional testimonials for the following company.

Name of Business: Fresh Bites Catering
Location: Chicago, IL
Services:
- Corporate Catering
- Event Planning
- Custom Menu Design
- Dietary Options

Company Highlights:
- Farm-to-table Ingredients
- Experienced Event Coordinators
- On-time Delivery

Testimonial:
"Fresh Bites Catering was the highlight of our corporate event in Chicago! The attention to detail in the custom menu,
 tailored to accommodate diverse dietary needs, was truly commendable.
 Their commitment to farm-to-table ingredients is reflected in every delicious bite.
 Plus, their event coordinators ensured everything went smoothly.
 On-time delivery with hot and fresh meals? They nailed it!"

##

Write an engaging and promotional testimonials for the following company.

Name of Business: Artistic Ink Tattoo Studio 
Location: Seattle, WA
Services:
- Custom Tattoos
- Cover-ups
- Body Piercing
- Tattoo Removal

Important Company Highlights:
- Award-winning Artists
- Strict Sanitary Standards
- Free Consultations

Testimonial:
"Artistic Ink Tattoo Studio in Seattle is where art meets soul.
Their award-winning artists transformed my vague idea into a masterpiece on my skin.
Their commitment to sanitation put my mind at ease, especially during my piercing session.
I appreciated the free consultation where we discussed design, placement,
and care. Whether it's a custom tattoo or a cover-up, Artistic Ink is the place to go!"

##

Write an engaging and promotional testimonials for the following company.

##

'''

WEBSITE_DESCRIPTION_FEW_SHOT = '''Write an engaging and promotional business description for the following company. Make sure that the Name of Business appears in the description.

Name of Business: Green Thumb Landscaping
Location: Portland, OR
Services:
- Landscape Design
- Lawn Maintenance
- Tree Pruning
- Irrigation Systems

Important Company Highlights:
- Eco-friendly practices
- Certified Arborists
- 100% Customer Satisfaction Guarantee

Description:
Enhance Your Outdoor Space with Professional Landscaping Services. From creative designs to sustainable maintenance,
Green Thumb Landscaping has you covered. 
Our certified arborists and irrigation experts ensure your landscape stays lush and beautiful year-round.
Experience the difference in Portland, OR!

##

Write an engaging and promotional business description for the following company. Make sure that the Name of Business appears in the description.

Name of Business: Tech Genie IT Solutions
Location: Austin, TX

Services:
- IT Consulting
- Network Security
- Cloud Services
- Data Backup & Recovery

Important Company Highlights:
- 24/7 IT Support
- Certified Technicians
- Customized Solutions for Businesses

Description:
Simplify Your IT with Tech Genie. Our team of certified technicians provides reliable IT solutions for businesses in Austin, TX.
From comprehensive network security to cloud services, we've got your back 24/7. Focus on your core business while we handle your tech needs.

##

Write an engaging and promotional business description for the following company. Make sure that the Name of Business appears in the description.

Name of Business: Fresh Bites Catering
Location: Chicago, IL

Services:
- Corporate Catering
- Event Planning
- Custom Menu Design
- Dietary Options

Company Highlights:
- Farm-to-table Ingredients
- Experienced Event Coordinators
- On-time Delivery

Description:
Elevate Your Events with Fresh Bites Catering. We bring a fresh twist to catering in Chicago, IL. 
Our farm-to-table ingredients and custom menu design ensure an unforgettable dining experience.
Our experienced event coordinators take care of all the details, so you can savor every moment.

##

Write an engaging and promotional business description for the following company. Make sure that the Name of Business appears in the description.

Name of Business: Artistic Ink Tattoo Studio 
Location: Seattle, WA

Services:
- Custom Tattoos
- Cover-ups
- Body Piercing
- Tattoo Removal

Important Company Highlights:
- Award-winning Artists
- Strict Sanitary Standards
- Free Consultations

Description:
Express Yourself with Artistic Ink Tattoos. Our award-winning artists in Seattle, WA, create unique and meaningful 
tattoos that tell your story. Safety is our top priority, with strict sanitary standards. 
Book a free consultation to discuss your tattoo ideas today!

##

Write an engaging and promotional business description for the following company. Make sure that the Name of Business appears in the description.

##

'''

WEBSITE_HEADLINE_FEW_SHOT = '''Write an engaging headline for the following company.

Name of Business: Juliana Laface Design

Description:
Every entrepreneur has a goal in mind when marketing their small business. Whether you want to increase your number of monthly website visitors, improve online sales, or book more consultations— you want to see a return on your investment.
As an Edmonton website designer, graphic designer and brand creator who also happens to be a small business owner, I have carefully considered each of my services, honing in on the offerings that provide my clients with the greatest gains.
Ultimately, I want to provide you with an unforgettable design, because that’s what I would want for my own business.

Headline:
Edmonton Website Designer, Graphic Designer & Brand Creator

##

Write an engaging headline for the following company.

Name of Business: Concept Marketing Group

Description:
Concept Marketing Group is a full-service licensing agency and recognized leader in targeted licensing, direct-to-retail, and other brand extension initiatives. Our experienced team provides valuable insight and guidance to licensee and licensor.
National and international icons of fashion, interior design and home furnishings, as well as charitable organizations have entrusted us with their brands.

Headline:
Proven Leaders in Brand Development & Licensing

##

Write an engaging headline for the following company.

Name of Business: The Frosting Room

Description:
Founded upon a passion for food and baking, The Bakery has become a one-stop shop for all kinds of delectable, gorgeous baked goods and then some. We have the perfect cup of coffee, freshly-made lunches and a plethora of tasty take away options, including granola, bagels, specialty breads and pizza.
If you’re in a hurry, a full palette of grab ‘n’ go desserts (think a giant chocolate cloud of mousse or a strawberry tarte) are available for your spontaneous dinner soiree.
From day one until today, this is what The Bakery does with a whole lot of love.

Headline:
One-stop shop for everything delicious

##

Write an engaging headline for the following company.

'''

OBQA_CONTEXT = """Large Language Models
Introduction to the core of our product

Natural language processing (NLP) has seen rapid growth in the last few years since large language models (LLMs) were introduced. Those huge models are based on the Transformers architecture, which allowed for the training of much larger and more powerful language models.
We divide LLMs into two main categories, Autoregressive and Masked LM (language model). In this page we will focus on Autoregressive LLMs, as our language models, Jurassic-1 series, belongs to this category.

⚡ The task: predict the next word
Autoregressive LLM is a neural network model composed from billions of parameters. It was trained on a massive amount of texts with one goal: to predict the next word, based on the given text. By repeating this action several times, every time adding the prediction word to the provided text, you will end up with a complete text (e.g. full sentences, paragraphs, articles, books, and more). In terms of terminology, the textual output (the complete text) is called a completion while the input (the given, original text) is called prompt.

🎓 Added value: knowledge acquisition
Imagine you had to read all of Shakespeare's works repeatedly to learn a language. Eventually, you would be able to not only memorize all of his plays and poems, but also imitate his writing style.
In similar fashion, we trained the LLMs by supplying them with many textual sources. This enabled them to gain an in-depth understanding of English as well as general knowledge.

🗣️ Interacting with Large Language Models
The LLMs are queried using natural language, also known as prompt engineering. 
Rather than writing lines of code and loading a model, you write a natural language prompt and pass it to the model as the input.

⚙️ Resource-intensive
Data, computation, and engineering resources are required for training and deploying large language models. LLMs, such as our Jurassic-1 models, play an important role here, providing access to this type of technology to academic researchers and developers.

Tokenizer & Tokenization

Now that you know what large language models are, you must be wondering: “How does a neural network use text as input and output?”.

The answer is: Tokenization 🧩
Any language can be broken down into basic pieces (in our case, tokens). Each of those pieces is translated into its own vector representation, which is eventually fed into the model. For example:
Each model has its own dictionary of tokens, which determines the language it "speaks". Each text in the input will be decomposed into these tokens, and every text generated by the model will be composed of them.
But how do we break down a language? Which pieces are we choosing as our tokens? There are several approaches to solve this:

🔡 Character-level tokenization
As a simple solution, each character can be treated as its own token. By doing so, we can represent the entire English language with just 26 characters (okay, double it for capital letters and add some punctuation). This would give us a small token dictionary, thereby reducing the width we need for those vectors and saving us some valuable memory. However, those tokens don’t have any inherent meaning - we all know what the meaning of “Cat” is, but what is the meaning of “C”? The key to understanding language is context. Although it is clear to us readers that a "Cat" and a "Cradle" have different meanings, for a language model with this tokenizer - the "C" is the same.

🆒 Word-level tokenization
Another approach we can try is breaking our text into words, just like in the example above ("I want to break free").
Now, every token has a meaning that the model can learn and use. We are gaining meaning, but that requires a much larger dictionary. Also, it raises another question: what about words stemming from the same root-word like ”helped”, “helping”, and “helpful”? In this approach each of these words will get a different token with no inherent relation between them, whereas for us readers it's clear that they all have a similar meaning.
Furthermore, words may have fundamentally different meanings when strung together - for instance, my run-down car isn't running anywhere. What if we went a step further?

💬 Sentence-level tokenization
In this approach we break our text into sentences. This will capture meaningful phrases! However, this would result in an absurdly large dictionary, with some tokens being so rare that we would require an enormous amount of data to teach the model the meaning of each token.

🏅 Which is best?
Each method has pros and cons, and like any real-life problem, the best solution involves a number of compromises. AI21 Studio uses a large token dictionary (250K), which contains some from every method: separate characters, words, word parts such as prefixes and suffixes, and many multi-word tokens."""

OBQA_QUESTION = "Which tokenization methods are there?"

DOC_QA = "What would you like to know?"
