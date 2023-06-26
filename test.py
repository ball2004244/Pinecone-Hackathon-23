from logic.pinecone_db import PineconeTrainer
from config import GCP_API_KEY, PINECONE_API_KEY, PINECONE_ENVIRONMENT
from logic.palm_ai import PalmAI

pinecone_trainer = PineconeTrainer(
    gcp_api_key=GCP_API_KEY,
    pinecone_api_key=PINECONE_API_KEY,
    pinecone_environment=PINECONE_ENVIRONMENT,
)

def create_index():
    input_file = 'logic/dataset.json'
    data = pinecone_trainer.extract_input_text(input_file)
    pinecone_trainer.add_data(data)

def get_info():
    info = pinecone_trainer.get_index_info()
    print(info)

def test_query():
    _input = 'Russia'
    output = pinecone_trainer.query(query=_input)

    print(output)


#! TEST VERTEX AI SUMMARIZER
palm_ai = PalmAI(GCP_API_KEY)

def test_palm():
    random_long_text = '''
    Russian coup could have reached Moscow outskirts without deal, experts say. Live updates
John Bacon
David Jackson
USA TODAY








Relative normalcy returned to Moscow on Sunday as Russian troops deployed to protect the capital withdrew following the retreat of the rebellious mercenary forces.

The brief insurgency, however, revealed the Kremlin's inability to provide an effective rapid response to the Wagner Group's advances, highlighting internal Russian security weaknesses, the Washington-based Institute for the Study of War said in its latest assessment. The Kremlin's struggle was likely the result of surprise combined with the impact of heavy losses in Ukraine, the assessment said. 

Wagner likely could have reached the outskirts of Moscow if Wagner leader Yevgheny Prigozhin had chosen to order them to do so, the assessment added. The march ended 300 miles from Moscow on Saturday with a deal between the Prigozhin and President Vladimir Putin.

On Sunday, roadblocks and checkpoints around the city had been removed and crowds swarmed the downtown area on a warm, sunny day, packing street cafés with customers, the Associated Press reported.

Still, the Biden administration is monitoring fallout from the coup attempt that could provide profound consequences for Vladimir Putin, Ukraine and Russia, Secretary of State Antony Blinken said Sunday.

"This is just the latest chapter in a book of failure that Putin has written for himself and for Russia," Blinken said on NBC News' "Meet the Press." "Economically, militarily, its standing in the world – all of those things have plummeted."

Will Vladimir Putin keep his grip on power? Coup attempt dials up pressure over Ukraine war

Russian soldiers walk past an area where the Wagner Group military company's tank was parked near the headquarters of the Southern Military District in Rostov-on-Don, southern Russia, on June 25, 2023.
Developments:

∙GOP presidential hopeful Chris Christie dismissed a recent Pew Research survey indicating 44% of Republicans and Republican-leaning independents say the U.S. is giving too much aid to Ukraine. "America has never been a great country and the leader of the world by filling in the moat and pulling up the drawbridge," said on ABC News' "This Week."

∙ Two more bodies were found under the rubble of a Kyiv apartment building a day after it was hit by missile debris during a Russian strike Saturday, Mayor Vitali Klitschko said Sunday. The discovery raises the death toll to five.

∙ Belarus President Alexander Lukashenko, apparently involved in negotiations that ended Prigozhin's march on Russia, could take part in negotiations to end the war, Ukraine Secretary of the National Security and Defense Council Alexei Danilov said on his Facebook page. "Lukashenko's participation in this process is not excluded," Danilov wrote.

What’s happening in Russia? Kremlin says Wagner chief to leave for Belarus after rebellion

Ukraine forces making 'gradual but steady' progress in war
Ukrainian forces have recently "re-set" and are pressing major offensive operations in southern and eastern Ukraine, the British Ministry of Defense says in it latest assessment of the war. Ukrainian forces are using the experiences from the first two weeks of the counter-offensive to refine tactics for assaulting the deep, well prepared Russian defenses an are making "gradual but steady tactical progress in key areas."

The assessment adds that in the Luhansk region, Russian forces have made a "significant effort" to launch an attack, probably a reflection of senior leadership orders to go on the offensive whenever possible.

"Russia has made some small gains, but Ukrainian forces have prevented a breakthrough," the assessment says.

Putin assures Russians he monitors war 24-7
Putin told a Russian TV audience he monitors the war around the clock. "Of course, I pay priority attention," he told journalist Pavel Zarubin on the "Moscow.Kremlin.Putin" TV program that aired Sunday. "This is how the day begins and this is how it ends."

When asked if he can get a report on important issues at 3 a.m., Putin said he "has been staying up quite late" due to what he calls the special military operation.

"Of course, I always have to be in touch. That's the way it goes. Always ... close by," he said.

Blinken sees 'real cracks' in Putin regime
Blinken, making the rounds on Sunday morning talk shows, said the chaotic events of recent days raise "profound questions" about Russia's invasion of Ukraine and revealed "real cracks" in Putin's regime. The agreement that persuaded a popular mercenary leader to abandon a march to Moscow doesn't end Putin's leadership crisis, Blinken said.

Blinken said officials are still trying to learn the details of the agreement between Putin and Yevgeny Prigozhin. The secretary of state did not comment on the stability of Putin's regime, or even whether he is still in Moscow. Asked about the security of Russia's massive nuclear stockpile, Blinken told CNN's "State of the Union" that is "something we're looking at very, very carefully."

He also said that "it’s too soon to tell where this is going to go."

China backs Putin's handling of rebellion
China's foreign ministry issues a statement Sunday expressing vague support of the deal struck by Putin and Prigozhin. Putin has been working for months to strengthen ties with China in the face of Russia's hostile relations with the West.

"This is Russia’s internal affair," the Chinese statement read. "As Russia’s friendly neighbor and comprehensive strategic partner of coordination for the new era, China supports Russia in maintaining national stability and achieving development and prosperity."

Revolt leader 'probably has got other arrows in the quiver'
An attempted coup against Russian President Vladimir Putin that was swiftly abandoned Saturday raised new questions about his grip on power and is expected to intensify pressure on him within Russia over the unpopular war in Ukraine. Putin had vowed a harsh penalty for Prigozhin, the head of the paramilitary force that has been fighting alongside Russia's regular army in Ukraine. But after Prigozhin abruptly ended the rebellion, the Kremlin said he would not be prosecuted and would instead leave for Belarus.

Although Putin's authority has not been challenged during his more than two decades as Russia's president, a shadowy group known as the siloviki – Russia’s version of the so-called Deep State security power brokers – wields substantial power behind the scenes in Russia, said Steven Hall, a former Moscow chief of station and head of Russia operations for the CIA. If Putin loses their support, he could be forced out almost immediately, he said.

"Putin and the Kremlin haven't played the last card yet," Hall said. "Neither have any of the other players here, including Prigozhin, who probably has got other arrows in the quiver."

− Josh Meyer

Wagner mercenaries begin retreat from Russian territory
Wagner militants were leaving the southern Russia region of Voronezh, a day after the group abandoned its armed march toward Moscow, local governor Alexander Gusev said Sunday. "The movement of Wagner units through Voronezh Oblast is ending," Gusev said in a Telegram post,adding that travel and social restrictions in the region will be lifted once "the situation is finally resolved."

Wagner militants had reportedly seized all of the regional capital Voronezh's military facilities after Prigozhin launched his rebellion "to restore justice" after alleging that a Russian missile strike on his mercenary forces' camps in Ukraine caused substantial casualties.
    '''

    palm_ai.summarize(random_long_text)
    palm_ai.save_to_file('summary.txt')
    print('Total time: %s' % palm_ai.ellapsed_time)

if __name__ == '__main__':
    test_palm()


