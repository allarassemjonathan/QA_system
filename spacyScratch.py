import spacy as s
from math import log2, factorial, sqrt
# from spacy.pipeline.textcat import DEFAULT_SINGLE_TEXTCAT_MODEL
# config = {
#    "threshold": 0.5,
#    "model": DEFAULT_SINGLE_TEXTCAT_MODEL,
# }
model = s.load("en_core_web_md")
# sample = """

# Considered it weak-kneed and unseemly to preserve food for the next day. 8 
# The natives of Australia are incapable of any labor whose reward is not 
# immediate; every Hottentot is a gentleman of leisure; and with the Bush- 
# men of Africa it is always “either a. feast or a famine.” 4 There is a mute 
# wisdom in this improvidence, as in many “savage” ways. The moment 
# man begins to take thought of the morrow he passes out of the Garden of 
# Eden into the vale of anxiety; the pale cast of worry settles down upon 
# him, greed is sharpened, property begins, and the good cheer of the 
# “thoughtless” native disappears. The American Negro is making this 
# transition today. “Of what are you thinking?” Peary asked one of his 
# Eskimo guides. “I do not have to think,” was the answer; “I have plenty 
# of meat.” Not to think unless we have to— there is much to be said for this 
# as the summation of wisdom. 

# Nevertheless, there were difficulties in this care-lessness, and those or- 
# ganisms that outgrew it came to possess a serious advantage in the struggle 
# for survival. The dog that buried .the bone which even a canine appetite 
# could not manage, the squirrel that gathered nuts for a later feast, the 
# bees that filled the comb with honey, the ants that laid up stores for a 
# rainy day— these were among the first creators of civilization. It was they, 
# or other subtle creatures like them, who taught our ancestors the art of 
# providing for tomorrow out of the surplus of today, or of preparing for 
# winter in summer’s time of plenty. 

# With what skill those ancestors ferreted out, from land and sea, the food 
# that was the basis of their simple societies! They grubbed edible things 
# from the earth with bare hands; they imitated or used the claws and tusks 
# of the animals, and fashioned tools out of ivory, bone or stone; they made 
# nets and traps and snares of rushes or fibre, and devised innumerable 
# artifices for fishing and hunting their prey. The Polynesians had nets a 
# thousand ells long, which could be handled only by a hundred men; in such 
# ways economic provision grew hand in hand with political organization, 
# and the united quest for food helped to generate the state. The Tlingit 
# fisherman put upon his head a cap like the head of a seal, and hiding his 
# body among the rocks, made a noise like a seal; seals came toward him, 
# and he speared them with the clear conscience of primitive war. Many 
# tribes threw narcotics into the streams to stupefy the fish into cooperation 
# with the fishermen; the Tahitians, for example, put into the water an in- 
# toxicating mixture prepared from the huteo nut or the hora plant; the 
# fish, drunk with it, floated leisurely on the surface, and were caught at the 



# 7 


# CHAP. Il) ECONOMIC ELEMENTS OF CIVILIZATION 

# anglers’ will. Australian natives, swimming under water while breathing 
# through a reed, pulled ducks beneath the surface by the legs, and gently 
# held them there till they were pacified. The Tarahumaras caught birds by 
# stringing kernels on tough fibres half buried under the ground; the birds 
# ate the kernels, and the Tarahumaras ate the birds. 6 

# Hunting is now to most of us a game, whose relish seems based upon 
# some mystic remembrance, in the blood, of ancient days when to hunter as 
# well as hunted it was a matter of life and death. For hunting was not 
# merely a quest for food, it was a war for security and mastery, a war 
# beside which all the wars of recorded history are but a little noise. In the 
# jungle man still fights for his life, for though there is hardly an animal 
# that will attack him unless it is desperate for food or cornered in the chase, 
# yet there is not always food for all, and sometimes only the fighter, or the 
# breeder of fighters, is allowed to eat. We see in our museums the relics 
# of that war of the species in the knives, clubs, spears, arrows, lassos, bolas, 
# lures, traps, boomerangs and slings with which primitive men won posses- 
# sion of the land, and prepared to transmit to an ungrateful posterity the 
# gift of security from every beast except man. Even today, after all 
# these wars of elimination, how many different populations move over the 
# earth! Sometimes, during a walk in the woods, one is awed by the variety 
# of languages spoken there, by the myriad species of insects, reptiles, carni- 
# vores and birds; one feels that man is an interloper on this crowded scene, 
# that he is the object of universal dread and endless hostility. Some day, 
# perhaps, these chattering quadrupeds, these ingratiating centipedes, these 
# insinuating bacilli, will devour man and all his works, and free the planet 
# from this marauding biped, these mysterious and unnatural weapons, these 
# careless feet! 

# Hunting and fishing were not stages in economic development, they 
# were modes of activity destined to survive into the highest forms of civil- 
# ized society. Once the center of life, they are still its hidden foundations; 
# behind our literature and philosophy, our ritual and art, stand the stout 
# killers of Packingtown. We do our hunting by proxy, not having the 
# stomach for honest killing in the fields; but our memories of the chase 
# linger in our joyful pursuit of anything weak or fugitive, and in the games 
# of our children— even in the word game. In the last analysis civilization is 
# based upon the food supply. The cathedral and the capitol, the museum 
# and the concert chamber, the library and the university are the fa£ade; 
# in the rear are the shambles. 



# 8 THE STORY OF CIVILIZATION (CHAP. II 

# To live by hunting was not original; if man had confined himself to 
# that he would have been just another carnivore. He began to be human 
# when out of the uncertain hunt he developed the greater security and 
# continuity of the pastoral life. For this involved advantages of high import- 
# ance: the domestication of animals, the breeding of cattle, and the use of 
# milk. We do not know when or how domestication began— perhaps when 
# the helpless young of slain beasts were spared and brought to the camp 
# as playthings for the children.” The animal continued to be eaten, but 
# not so soon; it acted as a beast of burden, but it was accepted almost demo- 
# cratically into the society of man; it became his comrade, and formed 
# with him a community of labor and residence. The miracle of reproduc- 
# tion was brought under control, and two captives were multiplied into a 
# herd. Animal milk released women from prolonged nursing, lowered 
# infantile mortality, and provided a new and dependable food. Population 
# increased, life became more stable and orderly, and the mastery of that 
# timid parvenu, man, became more secure on the earth. 

# Meanwhile woman was making the greatest economic discovery of 
# all— the bounty of the soil. While man hunted she grubbed about the tent 
# or hut for whatever edible things lay ready to her hand on the ground. In 
# Australia it was understood that during the absence of her mate on the 
# chase the wife would dig for roots, pluck fruit and nuts from the trees, 
# and collect honey, mushrooms, seeds and natural grains . 7 Even today, in 
# certain tribes of Australia, the grains that grow spontaneously out of the 
# earth are harvested without any attempt to separate and sow the seed; the 
# Indians of the Sacramento River Valley never advanced beyond this stage.” 
# We shall never discover when men first noted the function of the seed, and 
# turned collecting into sowing; such beginnings are the mysteries of his- 
# tory, about which we may believe and guess, but cannot know. It is 
# possible that when men began to collect unplanted grains, seeds fell along 
# the way between field and camp, and suggested at last the great secret 
# of growth. The Juangs threw the seeds together into the ground, leaving 
# them to find their own way up. The natives of Borneo put the seed into 
# holes which they dug with a pointed stick as they walked the fields.” The 
# simplest known culture of the earth is with this stick or “digger.” In Mada- 
# gascar fifty years ago the traveler could still see women armed with pointed 
# sticks, standing in a row like soldiers, and then, at a signal, digging their 
# sticks into the ground, turning over the soil, throwing in the seed, stamp- 
# ing the earth flat, and passing on to another furrow . 10 The second stage in 



# CHAP. Il) ECONOMIC ELEMENTS OF CIVILIZATION 9 

# complexity was culture with the hoe: the digging stick was tipped with 
# bone, and fitted with a crosspiece to receive the pressure of the foot. 
# When the Conquistadores arrived in Mexico they found that the Aztecs 
# knew no other tool of tillage than the hoe. With the domestication of 
# animals and the forging of metals a heavier implement could be used; the 
# hoe was enlarged into a plough, and the deeper turning of the soil revealed 
# a fertility in the earth that changed the whole career of man. Wild plants 
# were domesticated, new varieties were developed, old varieties were 
# improved. 

# Finally nature taught man the art of provision, the virtue of prudence,* 
# the concept of time. Watching woodpeckers storing acorns in the trees, 
# and the bees storing honey in hives, man conceived— perhaps after millen- 
# niums of improvident savagery— the notion of laying up food for the future. 
# He found ways of preserving meat by smoking it, salting it, freezing it; 
# better still, he built granaries secure from rain and damp, vermin and 
# thieves, and gathered food into them for the leaner months of the year. 
# Slowly it became apparent that agriculture could provide a better and 
# steadier food supply than hunting. With that realization man took one of 
# the three steps that led from the beast to civilization— speech, agriculture, 
# and writing. 

# It is not to be supposed that man passed suddenly from hunting to 
# tillage. Many tribes, like the American Indians, remained permanently 
# becalmed in the transition— the men given to the chase, the women tilling 
# the soil. Not only was the change presumably gradual, but it was never 
# complete. Man merely added a new way of securing food to an old way; 
# and for the most part, throughout his history, he has preferred the old 
# food to the new. We picture early man experimenting with a thousand 
# products of the earth to find, at much cost to his inward comfort, which 
# of them could be eaten safely; mingling these more and more with the 
# fruits and nuts, the flesh and fish he was accustomed to, but always yearn- 
# ing for the booty of the chase. Primitive peoples are ravenously fond of 
# meat, even when they live mainly on cereals, vegetables and milk . 11 
# If they come upon the carcass of a recently dead animal the result is likely 
# to be a wild debauch. Very often no time is wasted on cooking; the prey 
# is eaten raw, as fast as good teeth can tear and devour it; soon nothing is 
# left but the bones. Whole tribes have been known to feast for a week on a 


# Note the ultimate identity of the words provision , providence and prudence. 




# IO THE STORY OF CIVILIZATION (CHAP. H 

# whale thrown up on the shore." Though the Fuegians can cook, they 
# prefer their meat raw; when they catch a fish they kill it by biting it behind 
# the gills, and then consume it from head to tail without further ritual." 
# The uncertainty of the food supply made these nature peoples almost lit- 
# erally omnivorous: shellfish, sea urchins, frogs, toads, snails, mice, rats, 
# spiders, earthworms, scorpions, moths, centipedes, locusts, caterpillars, liz- 
# ards, snakes, boas, dogs, horses, roots, lice, insects, larvae, the eggs of rep- 
# tiles and birds— there is not one of these but was somewhere a delicacy, or 
# even a piece de resistance, to primitive men . 14 Some tribes are expert hunt- 
# ers of ants; others dry insects in the sun and then store them for a feast; 
# others pick the lice out of one another’s hair, and eat them with relish; 
# if a great number of lice can be gathered to make a petite marmite, they 
# are devoured with shouts of joy, as enemies of the human race . 15 The 
# menu of the lower hunting tribes hardly differs from that of the higher 
# apes . 15 

# The discovery of fire limited this indiscriminate voracity, and cooperated 
# with agriculture to free man from the chase. Cooking broke down the 
# cellulose and starch of a thousand plants indigestible in their raw state, 
# and man turned more and more to cereals and vegetables as his chief reli- 
# ance. At the same time cooking, by softening tough foods, reduced the 
# need of chewing, and began that decay of the teeth which is one of the 
# insignia of civilization. 

# To all the varied articles of diet that we have enumerated, man added 
# the greatest delicacy of all— his fellowman. Cannibalism was at one 
# time practically universal; it has been found in nearly all primitive tribes, 
# and among such later peoples as the Irish, the Iberians, the Piets, and the 
# eleventh-century Danes . 17 Among many tribes human flesh was a staple 
# of trade, and funerals were unknown. In the Upper Congo living men, 
# women and children were bought and sold frankly as articles of food ; 18 
# on the island of New Britain human meat was sold in shops as butcher’s 
# meat is sold among ourselves; and in some of the Solomon Islands human 
# victims, preferably women, were fattened for a feast like pigs . 10 The 
# Fuegians ranked women above dogs because, they said, “dogs taste of 
# otter.” In Tahiti an old Polynesian chief explained his diet to Pierre Loti: 
# “The white man, when well roasted, tastes like a ripe banana.” The Fiji- 
# ans, however, complained that the flesh of the whites was too salty and 
# tough, and that a European sailor was hardly fit to eat; a Polynesian tasted 
# better.” 



# II 


# CHAP. Il) ECONOMIC ELEMENTS OF CIVILIZATION 

# What was the origin of this practice? There is no surety that the 
# custom arose, as formerly supposed, out of a shortage of other food; if it 
# did, the taste once formed survived the shortage, and became a passionate 
# predilection.” Everywhere among nature peoples blood is regarded as a 
# delicacy— never with horror; even primitive vegetarians take to it with 
# gusto. Human blood is constantly drunk by tribes otherwise kindly and 
# generous; sometimes as medicine, sometimes as a rite or covenant, often 
# in the belief that it will add to the drinker the vital force of the victim . 22 
# No shame was felt in preferring human flesh; primitive man seems to have 
# recognized no distinction in morals between eating men and eating other 
# animals. In Melanesia the chief who could treat his friends to a dish of 
# roast man soared in social esteem. “When I have slain an enemy,” ex- 
# plained a Brazilian philosopher-chief, “it is surely better to eat him than 
# to let him waste. . . . The worst is not to be eaten, but to die; if I am 
# killed it is all the same whether my tribal enemy eats me or not. But I 
# could not think of any game that would taste better than he would. . . . 
# You whites are really too dainty .” 23 

# Doubtless the custom had certain social advantages. It anticipated Dean 
# Swift’s plan for the utilization of superfluous children, and it gave the old 
# an opportunity to die usefully. There is a point of view from which funer- 
# als seem an unnecessary extravagance. To Montaigne it appeared more 
# barbarous to torture a man to death under the cover of piety, as was the 
# mode of his time, than to roast and eat him after he was dead. We must 
# respect one another’s delusions. 

# II. THE FOUNDATIONS OF INDUSTRY 

# Fire— Primitive Tools— Weaving and pottery— Building and trans- 
# port— Trade and finance 

# If man began with speech, and civilization with agriculture, industry 
# began with fire. Man did not invent it; probably nature produced the 
# marvel for him by the friction of leaves or twigs, a stroke of lightning, or 
# a chance union of chemicals; man merely had the saving wit to imitate 
# nature, and to improve upon her. He put the wonder to a thousand uses. 
# First, perhaps, he made it serve as a torch to conquer his fearsome enemy, 
# the dark; then he used it for warmth, and moved more freely from his 
# native tropics to less enervating zones, slowly making the planet human; 
# then he applied it to metals, softening them, tempering them, and com- 



# 12 THE STORY OF CIVILIZATION (CHAP. II 

# bining them into forms stronger and suppler than those in which they had 
# come to his hand. So beneficent and strange was it that fire always re- 
# mained a miracle to primitive man, fit to be worshiped as a god; he offered 
# it countless ceremonies of devotion, and made it the center or focus (which 
# is Latin for hearth) of his life and home; he carried it carefully with him 
# as he moved from place to place in his wanderings, and would not will- 
# ingly let it die. Even the Romans punished with death the careless vestal 
# virgin who allowed the sacred fire to be extinguished. 

# Meanwhile, in the midst of hunting, herding and agriculture, invention 
# was busy, and the primitive brain was racking itself to find mechanical 
# answers to the economic puzzles of life. At first man was content, appar- 
# ently, to accept what nature offered him— the fruits of the earth as his 
# food, the skins and furs of the animals as his clothing, the caves in the 
# hillsides as his home. Then, perhaps (for most history is guessing, and the 
# rest is prejudice), he imitated the tools and industry of the animal: he saw 
# the monkey flinging rocks and fruit upon his enemies, or breaking open 
# nuts and oysters with a stone; he saw the beaver building a dam, the birds 
# making nests and bowers, the chimpanzees raising something very like a 
# hut. He envied the power of their claws, teeth, tusks and horns, and the 
# toughness of their hides; and he set to work to fashion tools and weapons 
# that would resemble and rival these. Man, said Franklin, is a tool-using 
# animal ; 31 but this, too, like the other distinctions on which we plume our- 
# selves, is only a difference of degree. 

# Many tools lay potential in the plant world that surrounded primitive 
# man. From the bamboo he made shafts, knives, needles and bottles; out of 
# branches he made tongs, pincers and vices; from bark and fibres he wove 
# cord and clothing of a hundred kinds. Above all, he made himself a stick. 
# It was a modest invention, but its uses were so varied that man always 
# looked upon it as a symbol of power and authority, from the wand of the 
# fairies and the staff of the shepherd to the rod of Moses or Aaron, the 
# ivory cane of the Roman consul, the lituus of the augurs, and the mace 
# of the magistrate or the king. In agriculture the stick became the hoe; in 
# war it became the lance or javelin or spear, the sword or bayonet . 35 Again, 
# man used the mineral world, and shaped stones into a museum of arms 
# and implements: hammers, anvils, kettles, scrapers, arrow-heads, saws, 
# planes, wedges, levers, axes and drills. From the animal world he made 
# ladles, spoons, vases, gourds, plates, cups, razors and hooks out of the 
# shells of the shore, and tough or dainty tools out of the horn or ivory, the 



# CHAP. II ) ECONOMIC ELEMENTS OF CIVILIZATION 13 

# teeth and bones, the hair and hide of the beasts. Most of these fashioned 
# articles had handles of wood, attached to them in cunning ways, bound 
# with braids of fibre or cords of animal sinew, and occasionally glued 
# with strange mixtures of blood. The ingenuity of primitive men prob- 
# ably equaled— perhaps it surpassed— that of the average modem man; we 
# differ from them through the social accumulation of knowledge, materials 
# and tools, rather than through innate superiority of brains. Indeed, nature 
# men delight in mastering the necessities of a situation with inventive wit. 
# It was a favorite game among the Eskimos to go off into difficult and de- 
# serted places, and rival one another in devising means for meeting the 
# needs of a life unequipped and unadorned.” 

# * This primitive skill displayed itself proudly in the art of weaving. Here, 
# too, the animal showed man the way. The web of the spider, the nest of 
# the bird, the crossing and texture of fibres and leaves in the natural em- 
# broidery of the woods, set an example so obvious that in all probability weav- 
# ing was one of the earliest arts of the human race. Bark, leaves and grass 
# fibres were woven into clothing, carpets and tapestry, sometimes so excellent 
# that it could not be rivaled today, even with the resources of contemporary 
# machinery. Aleutian women may spend a year in weaving one robe. The 
# blankets and garments made by the North American Indians were richly 
# ornamented with fringes and embroideries of hairs and tendon-threads dyed 
# in brilliant colors with berry juice; colors “so alive,” says Father Theodut, 
# “that ours do not seem even to approach them .” 21 Again art began where 
# nature left off; the bones of birds and fishes, and the slim shoots of the 
# bamboo tree, were polished into needles, and the tendons of animals were 
# drawn into threads ‘delicate enough to pass through the eye of the finest 
# needle today. Bark was beaten into mats and cloths, skins were dried for 
# clothing and shoes, fibres were twisted into the strongest yarn, and supple 
# branches and colored filaments were woven into baskets more beautiful than 
# any modem forms . 28 

# Akin to basketry, perhaps born of it, was the art of pottery. Clay placed 
# upon wickerwork to keep the latter from being burned, hardened into a 
# fireproof shell which kept its form when the wickerwork was taken away ; 29 
# this may have been the first stage of a development that was to culminate 
# in the perfect porcelains of China. Or perhaps some lumps of clay, baked 
# and hardened by the sun, suggested the ceramic art; it was but a step from 
# this to substitute fire for the sun, and to form from the earth myriad shapes 
# of vessels for every use— for cooking, storing and transporting, at last for 


# Reduced type, unindented, will be used occasionally for technical or dispensable matter. 



# H THE STORY OF CIVILIZATION (CHAP, n 

# luxury and ornament. Designs imprinted by finger-nail or tool upon the 
# wet clay were one of the first forms of art, and perhaps one of the origins 
# of writing. 

# Out of sun-dried clay primitive tribes made bricks and adobe, and dwelt, 
# so to speak, in pottery. But that was a late stage of the building art, bind- 
# ing the mud hut of the “savage” in a chain of continuous development with 
# the brilliant tiles of Nineveh and Babylon. Some primitive peoples, like the 
# Veddahs of Ceylon, had no dwellings at all, and were content with the 
# earth and the sky; some, like the Tasmanians, slept in hollow trees; some, 
# like the natives of New South Wales, lived in caves; others, like the Bush- 
# men, built here and there a wind-shelter of branches, or, more rarely, drove 
# piles into the soil and covered their tops with moss and twigs. From such 
# wind-shelters, when sides were added, evolved the hut, which is found 
# among the natives of Australia in all its stages from a tiny cottage of 
# branches, grass and earth large enough to cover two or three persons, to 
# great huts housing thirty or more. The nomad hunter or herdsman pre- 
# ferred a tent, which he could carry wherever the chase might lead him. 
# The higher type of nature peoples, like the American Indian, built with 
# wood; the Iroquois, for example, raised, out of timber still bearing the 
# bark, sprawling edifices five hundred feet long, which sheltered many fami- 
# lies. Finally, the natives of Oceania made real houses of carefully cut boards, 
# and the evolution of the wooden dwelling was complete . 80 

# Only three further developments were needed for primitive man to 
# create all the essentials of economic civilization: the mechanisms of trans- 
# port, the processes of trade, and the medium of exchange. The porter 
# carrying his load from a modem plane pictures the earliest and latest stages 
# in the history of transportation. In the beginning, doubtless, man was his 
# own beast of burden, unless he was married; to this day, for the most part, 
# in southern and eastern Asia, man is wagon and donkey and all. Then he 
# invented ropes, levers, and pulleys; he conquered and loaded the animal; 
# he made the first sledge by having his cattle draw along the ground long 
# branches bearing his goods;* he put logs as rollers under the sledge; he cut 
# cross-sections of the log, and made the greatest of all mechanical inven- 
# tions, the wheel; he put wheels under the sledge and made a cart. Other 
# logs he bound together as rafts, or dug into canoes; and the streams be- 
# came his most convenient avenues of transport. By land he went first 
# through trackless fields and hills, then by trails, at last by roads. He studied 
# the stars, and guided his caravans across mountains and deserts by tracing 

# * The American Indians, content with this device, never used the wheel. 



# CHAP. Il) ECONOMIC ELEMENTS OF CIVILIZATION 15 

# his route in the sky. He paddled, rowed or sailed his way bravely from 
# island to island, and at last spanned oceans to spread his modest culture 
# from continent to continent. Here, too, the main problems were solved 
# before written history began. 

# Since human skills and natural resources are diversely and unequally 
# distributed, a people may be enabled, by the development of specific talents, 
# or by its proximity to needed materials, to produce certain articles more 
# cheaply than its neighbors. Of such articles it makes more than it con- 
# sumes, and offers its surplus to other peoples in exchange for their own; 
# this is the origin of trade. The Chibcha Indians of Colombia exported 
# the rock salt that abounded in their territory, and received in return the 
# cereals that could not be raised on their barren soil. Certain American 
# Indian villages were almost entirely devoted to making arrow-heads; some 
# in New Guinea to making pottery; some in Africa to blacksmithing, or to 
# making boats or lances. Such specializing tribes or villages sometimes ac- 
# quired the names of their industry (Smith, Fisher, Potter . . . ), and these 
# names were in time attached to specializing families.” 8 Trade in surpluses 
# was at first by an interchange of gifts; even in our calculating days a 
# present (if only a meal) sometimes precedes or seals a trade. The ex- 
# change was facilitated by war, robbery, tribute, fines, and compensation; 
# goods had to be kept moving! Gradually an orderly system of barter 
# grew up, and trading posts, markets and bazaars were established— occa- 
# sionally, then periodically, then permanently— where those who had some 
# article in excess might offer it for some article of need.” 

# For a long time commerce was purely such exchange, and centuries 
# passed before a circulating medium of value was invented to quicken trade. 
# A Dyak might be seen wandering for days through a bazaar, with a ball of 
# beeswax in his hand, seeking a customer who could offer him in return 
# something that he might more profitably use.” The earliest mediums of 
# exchange were articles universally in demand, which anyone would take 
# in payment: dates, salt, skins, furs, ornaments, implements, weapons; in 
# such traffic two knives equaled one pair of stockings, all three equaled 
# a blanket, all four equaled a gun, all five equaled a horse; two elk-teeth 
# equaled one pony, and eight ponies equaled a wife.” There is hardly any 
# thing that has not been employed as money by some people at some time: 
# beans, fish-hooks, shells, pearls, beads, cocoa seeds, tea, pepper, at last 
# sheep, pigs, cows, and slaves. Cattle were a convenient standard of value 
# and medium of exchange among hunters and herders; they bore interest 



# 1 6 THE STORY OF CIVILIZATION (CHAP. II 

# through breeding, and they were easy to carry, since they transported 
# themselves. Even in Homer’s days men and things were valued in terms 
# of cattle: the armor of Diomedes was worth nine head of cattle, a skilful 
# slave was worth four. The Romans used kindred words— pecus and 
# pecunia— for cattle and money, and placed the image of an ox upon their 
# early coins. Our own words capital, chattel and cattle go back through 
# the French to the Latin capitate, meaning property: and this in turn 
# derives from caput, meaning head— i.e., of cattle. When metals were 
# mined they slowly replaced other articles as standards of value; copper, 
# bronze, iron, finally— because of their convenient representation of great 
# worth in little space and weight— silver and gold, became the money of 
# mankind. The advance from token goods to a metallic currency does not 
# seem to have been made by primitive men; it was left for the historic 
# civilizations to invent coinage and credit, and so, by further facilitating 
# the exchange of surpluses, to increase again the wealth and comfort of 
# man . 84 

# III. ECONOMIC ORGANIZATION 

# Primitive communism— Causes of its disappearance— Origins of 
# private property— Slavery— Classes 

# Trade was the great disturber of the primitive world, for until it came, 
# bringing money and profit in its wake, there was no property, and there- 
# fore little government. In the early stages of economic development 
# property was limited for the most part to things personally used; the 
# property sense applied so strongly to such articles that they (even the 
# wife) were often buried with their owner; it applied so weakly to things 
# not personally used that in their case the sense of property, far from being 
# innate, required perpetual reinforcement and inculcation. 

# Almost everywhere, among primitive peoples, land was owned by the 
# community. The North American Indians, the natives of Peru, the 
# Chittagong Hill tribes of India, the Borneans and South Sea Islanders seem 
# to have owned and tilled the soil in common, and to have shared the fruits 
# together. “The land,” said the Omaha Indians, “is like water and wind— 
# what cannot be sold.” In Samoa the idea of selling land was unknown 
# prior to the coming of the white man. Professor Rivers found communism 
# in land still existing in Melanesia and Polynesia; and in inner Liberia it 
# may be observed today . 85 

# Only less widespread was communism in food. It was usual among 



# i7 


# CHAP. Il) ECONOMIC ELEMENTS OF CIVILIZATION 

# “savages” for the man who had food to share it with the man who had 
# none, for travelers to be fed at any home they chose to stop at on their 
# way, and for communities harassed with drought to be maintained by 
# their neighbors . 30 If a man sat down to his meal in the woods he was 
# expected to call loudly for some one to come and share it with him, before 
# he might justly eat alone . 11 When Turner told a Samoan about the poor in 
# London the “savage” asked in astonishment: “How is it? No food? No 
# friends? No house to live in? Where did he grow? Are there no 
# houses belonging to his friends ?” 38 The hungry Indian had but to ask to 
# receive; no matter how small the supply was, food was given him if he 
# needed it; “no one can want food while there is com anywhere in the 
# town .” 30 Among the Hottentots it was the custom for one who had more 
# than others to share his surplus till all were equal. White travelers in 
# Africa before the advent of civilization noted that a present of food or 
# other valuables to a “black man” was at once distributed; so that when 
# a suit of clothes was given to one of them the donor soon found the 
# recipient wearing the hat, a friend the trousers, another friend the coat. 
# The Eskimo hunter had no personal right to his catch; it had to be divided 
# among the inhabitants of the village, and tools and provisions were the 
# common property of all. The North American Indians were described 
# by Captain Carver as “strangers to all distinctions of property, except in 
# the articles of domestic use. . . . They are extremely liberal to each other, 
# and supply the deficiencies of their friends with any superfluity of their 
# own.” “What is extremely surprising,” reports a missionary, “is to see 
# them treat one another with a gentleness and consideration which one does 
# not find among common people in the most civilized nations. This, doubt- 
# less, arises from the fact that the words ‘mine’ and ‘thine,’ which St. 
# Chrysostom says extinguish in our hearts the fire of charity and kindle 
# that of greed, are unknown to these savages.” “I have seen them,” says 
# another observer, “divide game among themselves when they sometimes 
# had many shares to make; and cannot recollect a single instance of their 
# falling into a dispute or finding fault with the distribution as being unequal 
# or otherwise objectionable. They would rather lie down themselves on 
# an empty stomach than have it laid to their charge that they neglected 
# to satisfy the needy. . . . They look upon themselves as but one great 
# family .” 40 

# Why did this primitive communism disappear as men rose to what we, 
# with some partiality, call civilization? Sumner believed that communism 



# l8 THE STORY OF CIVILIZATION (CHAP. H 

# proved unbiological, a handicap in the struggle for existence; that it gave 
# insufficient stimulus to inventiveness, industry and thrift; and that the 
# failure to reward the more able, and punish the less able, made for a level- 
# ing of capacity which was hostile to growth or to successful competition 
# with other groups." Loskiel reported some Indian tribes of the northeast 
# as “so lazy that they plant nothing themselves, but rely entirely upon the 
# expectation that others will not refuse to share their produce with them. 
# Since the industrious thus enjoy no more of the fruits of their labor than 
# the idle, they plant less every year.”" Darwin thought that the perfect 
# equality among the Fuegians was fatal to any hope of their becoming 
# civilized; 49 or, as the Fuegians might have put it, civilization would have 
# been fatal to their equality. Communism brought a certain security to all 
# who survived the diseases and accidents due to the poverty and ignorance 
# of primitive society; but it did not lift them out of that poverty. In- 
# dividualism brought wealth, but it brought, also, insecurity and slavery; 
# it stimulated the latent powers of superior men, but it intensified the com- 
# petition of life, and made men feel bitterly a poverty which, when all 
# shared it alike, had seemed to oppress none.* 

# Communism could survive more easily in societies where men were 
# always on the move, and danger and want were ever present. Hunters 
# and herders had no need of private property in land; but when agriculture 
# became the settled life of men it soon appeared that the land was most 
# fruitfully tilled when the rewards of careful husbandry accrued to the 
# family that had provided it. Consequently— since there is a natural selec- 
# tion of institutions and ideas as well as of organisms and groups— the 
# passage from hunting to agriculture brought a change from tribal property 
# to family property; the most economical unit of production became the 

# * Perhaps one reason why communism tends to appear chiefly at the beginning of civili- 
# zations is that it flourishes most readily in times of dearth, when the common danger of 
# starvation fuses the individual into the group. When abundance comes, and the danger 
# subsides, social cohesion is lessened, and individualism increases; communism ends where 
# luxury begins. As the life of a society becomes more complex, and the division of labor 
# differentiates men into diverse occupations and trades, it becomes more and more unlikely 
# that all these services will be equally valuable to the group; inevitably those whose greater 
# ability enables them to perform the more vital functions will take more than their equal 
# share of the rising wealth of the group. Every growing civilization is a scene of multiply- 
# ing inequalities; the natural differences of human endowment unite with differences of 
# opportunity to produce artificial differences of wealth and power; and where no laws or 
# despots suppress these artificial inequalities they reach at last a bursting point where the 
# poor have nothing to lose by violence, and the chaos of revolution levels men again into a 
# community of destitution. 

# Hence the dream of communism lurks in every modem society as a racial memory of a 



# CHAP. Il) ECONOMIC ELEMENTS OF CIVILIZATION 19 

# unit of ownership. As the family took on more and more a patriarchal 
# form, with authority centralized in the oldest male, property became 
# increasingly individualized, and personal bequest arose. Frequently an 
# enterprising individual would leave the family haven, adventure beyond 
# the traditional boundaries, and by hard labor reclaim land from the forest, 
# the jungle or the marsh; such land he guarded jealously as his own, and 
# in the end society recognized his right, and another form of individual 
# property began."* As the pressure of population increased, and older 
# lands were exhausted, such reclamation went on in a widening circle, until, 
# in the more complex societies, individual ownership became the order of 
# the day. The invention of money cooperated with these factors by facili- 
# tating the accumulation, transport and transmission of property. The 
# old tribal rights and traditions reasserted themselves in the technical owner- 
# ship of the soil by the village community or the king, and in periodical 
# redistributions of the land; but after an epoch of natural oscillation between 
# the old and the new, private property established itself definitely as the 
# basic economic institution of historical society. 

# Agriculture, while generating civilization, led not only to private prop- 
# erty but to slavery. In purely hunting communities slavery had been 
# unknown; the hunter’s wives and children sufficed to do the menial work. 
# The men alternated between the excited activity of hunting or war, and 
# the exhausted lassitude of satiety or peace. The characteristic laziness 
# of primitive peoples had its origin, presumably, in this habit of slowly re- 
# cuperating from the fatigue of battle or the chase; it was not so much 
# laziness as rest. To transform this spasmodic activity into regular work 
# two things were needed: the routine of tillage, and the organization of 
# labor. 

# Such organization remains loose and spontaneous where men are work- 
# ing for themselves; where they work for others, the organization of labor 


# simpler and more equal life; and where inequality or insecurity rises beyond sufferance, 
# men welcome a return to a condition which they idealize by recalling its equality and. 
# forgetting its poverty. Periodically the land gets itself redistributed, legally or not, 
# whether by the Gracchi in Rome, the Jacobins in France, or the Communists in Russia; 
# periodically wealth is redistributed, whether by the violent confiscation of property, or 
# by confiscatory taxation of incomes and bequests. Then the race for wealth, goods and 
# power begins again, and the pyramid of ability takes form once more; under whatever 
# laws may be enacted the abler man manages somehow to get the richer soil, the better 
# place, the lion’s share; soon he is strong enough to dominate the state and rewrite or 
# interpret the laws; and in time the inequality is as great as before. In this aspect all 
# economic history is the slow heart-beat of the social organism, a vast systole and diastole 
# of naturally concentrating wealth and naturally explosive revolution. 



# 20 THE STORY OF CIVILIZATION (CHAP. II 

# depends in the last analysis upon force. The rise of agriculture and the 
# inequality of men led to the employment of the socially weak by the 
# socially strong; not till then did it occur to the victor in war that the only 
# good prisoner is a live one. Butchery and cannibalism lessened, slavery 
# grew . 44 It was a great moral improvement when men ceased to kill or 
# eat their fellowmen, and merely made them slaves. A similar develop- 
# ment on a larger scale may be seen today, when a nation victorious in war 
# no longer exterminates the enemy, but enslaves it with indemnities. Once 
# slavery had been established and had proved profitable, it was extended 
# by condemning to it defaulting debtors and obstinate criminals, and by 
# raids undertaken specifically to capture slaves. War helped to make 
# slavery, and slavery helped to make war. 

# Probably it was through centuries of slavery that our race acquired 
# its traditions and habits of toil. No one would do any hard or persistent 
# work if he could avoid it without physical, economic or social penalty. 
# Slavery became part of the discipline by which man was prepared for 
# industry. Indirectly it furthered civilization, in so far as it increased 
# wealth and— for a minority— created leisure. After some centuries men 
# took it for granted; Aristotle argued for slavery as natural and inevitable, 
# and St. Paul gave his benediction to what must have seemed, by his time, 
# a divinely ordained institution. 

# Gradually, through agriculture and slavery, through the division of 
# labor and the inherent diversity of men, the comparative equality of 
# natural society was replaced by inequality and class divisions. “In the 
# primitive group we find as a rule no distinction between slave and free, 
# no serfdom, no caste, and little if any distinction between chief and 
# followers .” 45 Slowly the increasing complexity of tools and trades sub- 
# jected the unskilled or weak to the skilled or strong; every invention was 
# a new weapon in the hands of the strong, and further strengthened them 
# in their mastery and use of the weak.* Inheritance added superior oppor- 
# tunity to superior possessions, and stratified once homogeneous societies 
# into a maze of classes and castes. Rich and poor became disruptively 
# conscious of wealth and poverty; the class war began to run as a red 
# thread through all history; and the state arose as an indispensable instru- 
# ment for the regulation of classes, the protection of property, the waging 
# of war, and the organization of peace. 


# * So in our time that Mississippi of inventions which we call the Industrial Revolution 
# has enormously intensified the natural inequality of men. 


# CHAPTER III 


# The Political Elements of Civilization 

# I. THE ORIGINS OF GOVERNMENT 

# The unsocial instinct— Primitive anarchism— The clan and the 
# tribe— The king— War 

# M AN is not willingly a political animal. The human male associates 
# with his fellows less by desire than by habit, imitation, and the 
# compulsion of circumstance; he does not love society so much as he 
# fears solitude. He combines with other men because isolation endangers 
# him, and because there are many things that can be done better together 
# than alone; in his heart he is a solitary individual, pitted heroically against 
# the world. If the average man had had his way there would probably 
# never have been any state. Even today he resents it, classes death with 
# taxes, and yearns for that government which governs least. If he asks 
# for many laws it is only because he is sure that his neighbor needs them; 
# privately he is an unphilosophical anarchist, and thinks laws in his own 
# case superfluous. 

# In the simplest societies there is hardly any government. Primitive 
# hunters tend to accept regulation only when they join the hunting pack 
# and prepare for action. The Bushmen usually live in solitary families; 
# the Pygmies of Africa and the simplest natives of Australia admit only 
# temporarily of political organization, and then scatter away to their 
# family groups; the Tasmanians had no chiefs, no laws, no regular govern- 
# ment; the Veddahs of Ceylon formed small circles according to family 
# relationship, but had no government; the Kubus of Sumatra “live without 
# men in authority,” every family governing itself; the Fuegians are seldom 
# more than twelve together; the Tungus associate sparingly in groups of 
# ten tents or so; the Australian “horde” is seldom larger than sixty souls . 1 
# In such cases association and cooperation are for special purposes, like 
# hunting; they do not rise to any permanent political order. 

# The earliest form of continuous social organization was the clan— a group 
# of related families occupying a common tract of land, having the same 

# 21 



# 22 THE STORY OF CIVILIZATION (CHAP. Ill 

# totem, and governed by the same customs or laws. When a group of clans 
# united under the same chief the tribe was formed, and became the second 
# step on the way to the state. But this was a slow development; many 
# groups had no chiefs at all,’ and many more seem to have tolerated them 
# only in time of war.* Instead of democracy being a wilted feather in the 
# cap of our own age, it appears at its best in several primitive groups where 
# such government as exists is merely the rule of the family-heads of the 
# clan, and no arbitrary authority is allowed.* The Iroquois and Delaware 
# Indians recognized no laws or restraints beyond the natural order of the 
# family and die clan; their chiefs had modest powers, which might at any 
# time be ended by the elders of the tribe. The Omaha Indians were ruled 
# by a Council of Seven, who deliberated until they came to a unanimous 
# agreement; add this to the famous League of the Iroquois, by which many 
# tribes bound themselves— and honored their pledge— to keep the peace, 
# and one sees no great gap between these “savages” and the modem states 
# that bind themselves revocably to peace in the League of Nations. 

# It is war that makes the chief, the king and the state, just as it is these 
# that make war. In Samoa the chief had power during war, but at other 
# times no one paid much attention to him. The Dyaks had no other 
# government than that of each family by its head; in case of strife they 
# chose their bravest warrior to lead them, and obeyed him strictly; but 
# once the conflict was ended they literally sent him about his business.* 
# In the intervals of peace it was the priest, or head magician, who had most 
# authority and influence; and when at last a permanent kingship developed 
# as the usual mode of government among a majority of tribes, it combined— 
# and derived from— the offices of warrior, father and priest. Societies are 
# ruled by two powers: in peace by the word, in crises by the sword; force 
# is used only when indoctrination fails. Law and myth have gone hand in 
# hand throughout the centuries, cooperating or taking turns in the manage- 
# ment of mankind; until our own day no state dared separate them, and 
# perhaps tomorrow they will be united again. 

# How did war lead to the state? It is not that men were naturally in- 
# clined to war. Some lowly peoples are quite peaceful; and the Eskimos 
# could not understand why Europeans of the same pacific faith should hunt 
# one another like seals and steal one another’s land. “How well it is”— 
# they apostrophized their soil— “that you are covered with ice and snow! 
# How well it is that if in your rocks there are gold and silver, for which 
# the Christians are so greedy, it is covered with so much snow that they 



# CHAP. Ill) POLITICAL ELEMENTS OF CIVILIZATION 23 

# cannot get at it! Your unfruitfulness makes us happy, and saves us from 
# molestation .” 0 Nevertheless, primitive life was incarnadined with inter- 
# mittent war. Hunters fought for happy hunting grounds still rich in 
# prey, herders fought for new pastures for their flocks, tillers fought for 
# virgin soil; all of them, at times, fought to avenge a murder, or to harden 
# and discipline their youth, or to interrupt the monotony of life, or for 
# simple plunder and rape; very rarely for religion. There were institutions 
# and customs for the limitation of slaughter, as among ourselves— certain 
# hours, days, weeks or months during which no gentleman savage would 
# kill; certain functionaries who were inviolable, certain roads neutralized, 
# certain markets and asylums set aside for peace; and the League of the 
# Iroquois maintained the “Great Peace” for three hundred years . 7 But 
# for the most part war was the favorite instrument of natural selection 
# among primitive nations and groups. 

# Its results were endless. It acted as a ruthless eliminator of weak peoples, 
# and raised the level of the race in courage, violence, cruelty, intelligence 
# and skill. It stimulated invention, made weapons that became useful tools, 
# and arts of war that became arts of peace. (How many railroads today 
# begin in strategy and end in trade!) Above all, war dissolved primitive 
# communism and anarchism, introduced organization and discipline, and 
# led to the enslavement of prisoners, the subordination of classes, and the 
# growth of government. Property was the mother, war was the father, 
# of the state. 

# II. THE STATE 

# As the organization of force— The village community— The 
# psychological aides of the state 

# “A herd of blonde beasts of prey,” says Nietzsche, “a race of con- 
# querors and masters, which with all its warlike organization and all its 
# organizing power pounces with its terrible claws upon a population, in 
# numbers possibly tremendously superior, but as yet formless, . . . such 
# is the origin of the state .” 8 “The state as distinct from tribal organization,” 
# says Lester Ward, “begins with the conquest of one race by another .” 8 
# “Everywhere,” says Oppenheimer, “we find some warlike tribe breaking 
# through the -boundaries of some less warlike people, settling down as 
# nobility, and founding its state .” 18 “Violence,” says Ratzenhofer, “is the 
# agent which has created the state .” 11 The state, says Gumplowicz, is 
# the result of conquest, the establishment of the victors as a ruling caste 



# 24 THE STORY OF CIVILIZATION (CHAP. Ill 

# over the vanquished. 13 “The state,” says Sumner, “is the product of 
# force, and exists by force.” 13 

# This violent subjection is usually of a settled agricultural group by a 
# tribe of hunters and herders. 14 For agriculture teaches men pacific ways, 
# inures them to a prosaic routine, and exhausts them with the long day’s 
# toil; such men accumulate wealth, but they forget the arts and sentiments 
# of war. The hunter and the herder, accustomed to danger and skilled 
# in killing, look upon war as but another form of the chase, and hardly 
# more perilous; when the woods cease to give them abundant game, or 
# flocks decrease through a thinning pasture, they look with envy upon the 
# ripe fields of the village, they invent with modem ease some plausible 
# reason for attack, they invade, conquer, enslave and rule.* 


# The state is a late development, and hardly appears before the time of 
# written history. For it presupposes a change in the very principle of social 
# organization— from kinship to domination; and in primitive societies the 
# former is the rule. Domination succeeds best where it binds diverse natural 
# groups into an advantageous unity of order and trade. Even such conquest 
# is seldom lasting except where the progress of invention has strengthened 
# the strong by putting into their hands new tools and weapons for suppress- 
# ing revolt. In permanent conquest the principle of domination tends to be- 
# come concealed and almost unconscious; the French who rebelled in 1789 
# hardly realized, until Camille Desmoulins reminded them, that the aris- 
# tocracy that had ruled them for a thousand years had come from Germany 
# and had subjugated them by force. Time sanctifies everything; even the 
# most arrant theft, in the hands of the robber’s grandchildren, becomes sacred 
# and inviolable property. Every state begins in compulsion; but the habits 
# of obedience become the content of conscience, and soon every citizen 
# thrills with loyalty to the flag. 

# The citizen is right; for however the state begins, it soon becomes an in- 
# dispensable prop to order. As trade unites clans and tribes, relations spring 
# up that depend not on kinship but on contiguity, and therefore require an 
# artificial principle of regulation. The village community may serve as an 
# example: it displaced tribe and clan as the mode of local organization, and 

# • It is a law that holds only for early societies, since under more complex conditions a 
# variety of other factors— greater wealth, better weapons, higher intelligence— contribute to 
# determine the issue. So Egypt was conquered not only by Hyksos, Ethiopian, Arab and 
# Turkish nomads, but also by the settled civilizations of Assyria, Persia, Greece, Rome and 
# England— though not until these nations had become hunters and nomads on an imperial- 
# istic scale. 




# CHAP. Ill) POLITICAL ELEMENTS OF CIVILIZATION 25 

# achieved a simple, almost democratic government of small areas through a 
# concourse of family-heads; but the very existence and number of such com- 
# munities created a need for -come external force that could regulate their 
# interrelations and weave them into a larger economic web. The state, ogre 
# though it was in its origin, supplied this need; it became not merely an or- 
# ganized force, but an instrument for adjusting the interests of the thousand 
# conflicting groups that constitute a complex society. It spread the tentacles of 
# its power and law over wider and wider areas, and though it made external 
# war more destructive than before, it extended and maintained internal peace; 
# the state may be defined as internal peace for external war. Men decided 
# that it was better to pay taxes than to fight among themselves; better to pay 
# tribute to one magnificent robber than to bribe them all. What an inter- 
# regnum meant to a society accustomed to government may be judged from 
# the behavior of the Baganda, among whom, when the king died, every man 
# had to arm himself; for the lawless ran riot, killing and plundering every- 
# where . 15 “Without autocratic rule,” as Spencer said, “the evolution of so- 
# ciety could not have commenced .” 18 

# A state which should rely upon force alone would soon fall, for though 
# men are naturally gullible they are also naturally obstinate, and power, 
# like taxes, succeeds best when it is invisible and indirect. Hence the state, 
# in order to maintain itself, used and forged many instruments of in- 
# doctrination— the family, the church, the school— to build in the soul of 
# the citizen a habit of patriotic loyalty and pride. This saved a thousand 
# policemen, and prepared the public mind for that docile coherence which 
# is indispensable in war. Above all, the ruling minority sought more and 
# more to transform its forcible mastery into a body of law which, while 
# consolidating that mastery, would afford a welcome security and order 
# to the people, and would recognize the rights of the “subject”* sufficiently 
# to win his acceptance of the law and his adherence to the State. 

# III. LAW 

# Law-lessness—Law and custom— Revenge— Fines— Courts— Ordeal 
# — The duel— Punishment— Primitive freedom 

# Law comes with property, marriage and government; the lowest societies 
# manage to get along without it. “I have lived with communities of savages 
# in South America and in the East,” said Alfred Russel Wallace, “who 


# Note how this word betrays the origin of the state. 



# 26 THE STORY OF CIVILIZATION (CHAP. Ill 

# have no law or law-courts but the public opinion of the village freely 
# expressed. Each man scrupulously respects the rights of his fellows, and 
# any infraction of those rights rarely or never takes place. In such a com- 
# munity all are nearly equal .” 17 Herman Melville writes similarly of the 
# Marquesas Islanders: “During the time I have lived among the Typees 
# no one was ever put upon his trial for any violence to the public. Every- 
# thing went on in the valley with a harmony and smoothness unparalleled, 
# I will venture to assert, in the most select, refined, and pious associations' 
# of mortals in Christendom .” 18 The old Russian Government established 
# courts of law in the Aleutian Islands, but in fifty years those courts found 
# no employment. “Crime and offenses,” reports Brinton, “were so infre- 
# quent under the social system of the Iroquois that they can scarcely be 
# said to have had a penal code .” 19 Such are the ideal— perhaps the idealized— 
# conditions for whose return the anarchist perennially pines. 

# Certain amendments must be made to these descriptions. Natural socie- 
# ties are comparatively free from law first because they are ruled by cus- 
# toms as rigid and inviolable as any law; and secondly because crimes of 
# violence, in the beginning, are considered to be private matters, and are left 
# to bloody personal revenge. 

# Underneath all the phenomena of society is the great terra flrma of cus- 
# tom, that bedrock of time-hallowed modes of thought and action which 
# provides a society with some measure of steadiness and order through all 
# absence, changes, and interruptions of law. Custom gives the same stability 
# to the group that heredity and instinct give to the species, and habit to the 
# individual. It is the routine that keeps men sane; for if there were no grooves 
# along which thought and action might move with unconscious ease, the 
# mind would be perpetually hesitant, and would soon take refuge in lunacy. 
# A law of economy works in instinct and habit, in custom and convention: 
# the most convenient mode of response to repeated stimuli or traditional sit- 
# uations is automatic response. Thought and innovation are disturbances of 
# regularity, and are tolerated only for indispensable readaptations, or 
# promised gold. * 
# """

config = {"punct_chars": None}
model.add_pipe("sentencizer", config=config)

# sample_doc = model(sample)

# clean_sample = [t for t in sample_doc if not t.is_stop and not t.is_punct and not t.is_space]
# for t in clean_sample:
#     print(t.lemma_,t.pos_)

# data = s.displacy.render(sample_doc,style='dep',jupyter=False)
# with open("data.html", "w") as file:
#     file.write(data)

#clean_sample.ents - .text and .label_

# key = model("apocryphal")
# max_sim = 0
# max_sim_t = ""
# for t in clean_sample:
#     sim = 0
#     if t.has_vector:
#         sim = t.similarity(key)
#     if sim > max_sim:
#         max_sim = sim
#         max_sim_t = t
# print(max_sim_t,max_sim_t.similarity(key))

# model.add_pipe('textcat', config=config)
# print(model.pipe_names)

#Sentencizer
# i = 0
# for s in sample_doc.sents:
#     if i == 1:
#         break
#     i += 1
#     # print(s,type(s))
#     # print(len(s))
#     # for t in s:
#     #     if not t.is_punct and not t.is_space and not t.is_stop:
#     #         print(t.lemma_)
#     print("##################################")
# print(len(list(sample_doc.sents)))
def coherence(s):
    c = 0
    curdex = 0
    checkdex = 0
    times = 0
    clean_s = [t for t in s if not t.is_stop and not t.is_punct and not t.is_space and t.has_vector]
    size = len(clean_s)
    for t1 in s:
        for t2 in s:
            if t1 != t2 and checkdex > curdex and t1.has_vector and t2.has_vector and not t1.is_stop and not t1.is_punct and not t1.is_space and not t2.is_punct and not t2.is_stop and not t2.is_space:
                c += t1.similarity(t2)
            checkdex += 1
            times += 1
        checkdex = 0
        curdex += 1
    # print("SIZE:",size)
    if times != 0 and size > 1:
        return ((2*size)/(size-1))*(c/times)
    else:
        return 1.0

# def how_similar(s1,s2): #iterable with len() of tokens w/o stops, punct, and space
#     size1 = len(s1)
#     size2 = len(s2)
#     # c1 = coherence(s1)
#     # c2 = coherence(s2)
#     sum_sim = 0
#     for t1 in s1:
#         for t2 in s2:
#             if t1.has_vector and t2.has_vector:
#                 sum_sim += t1.similarity(t2)
#     # avg_sim = sum_sim/(log2(size2*size1 + 1))
#     avg_sim = sum_sim/(size1*size2)
#     # avg_sim = (sum_sim/(size1*size2))/(c1*c2)
#     return avg_sim

# def how_similar2(s1,s2):
#     size1 = len(s1)
#     size2 = len(s2)
#     # c1 = coherence(s1)
#     # c2 = coherence(s2)
#     prod_sim = 1
#     for t1 in s1:
#         for t2 in s2:
#             if t1.has_vector and t2.has_vector:
#                 prod_sim *= t1.similarity(t2)
#                 print(prod_sim)
#                 if prod_sim == 0:
#                     return
#     return (prod_sim*size1*size2)**(1/10)

# i = 0
# for sent in sample_doc.sents:
#     if i == 2:
#         break
#     if i == 0:
#         s1 = sent
#     if i == 1:
#         s2 = sent
#     i += 1
# s1 = model("The engine is galvanized.")
# s1 = model("My ugly baby has diaper rash and needs a binky.")
# s1 = model("The jacket speaks Swahili in a mechanic's noodles.")
# s1 = model("station flatulent station flatulent")
# s1 = model("Diesel engine diesel engine diesel engine")
s1 = model("When was Colonel Sanders born?")
# s1 = model("Several legends surround Alexander's birth and childhood.")
# s2 = model("Several legends surround Alexander's birth and childhood. According to the ancient Greek biographer Plutarch, on the eve of the consummation of her marriage to Philip, Olympias dreamed that her womb was struck by a thunderbolt that caused a flame to spread 'far and wide' before dying away. Sometime after the wedding, Philip is said to have seen himself, in a dream, securing his wife's womb with a seal engraved with a lion's image. Plutarch offered a variety of interpretations for these dreams: that Olympias was pregnant before her marriage, indicated by the sealing of her womb; or that Alexander's father was Zeus. Ancient commentators were divided about whether the ambitious Olympias promulgated the story of Alexander's divine parentage, variously claiming that she had told Alexander, or that she dismissed the suggestion as impious.")
# s2 = model("My dog is a very obedient canine who is trained to heel and bury bones.")
s3 = model("Alexander was born in 356 BCE at Pella in Macedonia, the son of Philip II and Olympias (daughter of King Neoptolemus of Epirus).")
# s3 = model("He was born in 356 BCE at Pella in Macedonia, the son of Philip II and Olympias (daughter of King Neoptolemus of Epirus). From age 13 to 16 he was taught by Aristotle, who inspired him with an interest in philosophy, medicine, and scientific investigation, but he was later to advance beyond his teacher’s narrow precept that non-Greeks should be treated as slaves. Left in charge of Macedonia in 340 during Philip’s attack on Byzantium, Alexander defeated the Maedi, a Thracian people. Two years later he commanded the left wing at the Battle of Chaeronea, in which Philip defeated the allied Greek states, and displayed personal courage in breaking the Sacred Band of Thebes, an elite military corps composed of 150 pairs of lovers. A year later Philip divorced Olympias, and, after a quarrel at a feast held to celebrate his father’s new marriage, Alexander and his mother fled to Epirus, and Alexander later went to Illyria. Shortly afterward, father and son were reconciled and Alexander returned, but his position as heir was jeopardized.")
s4 = model("Hannibal was born in what is present day northern Tunisia, one of many Mediterranean regions colonised by the Canaanites from their homelands in Phoenicia.")
# s4 = model("Hannibal was one of the sons of Hamilcar Barca, a Carthaginian leader, and an unknown mother. He was born in what is present day northern Tunisia, one of many Mediterranean regions colonised by the Canaanites from their homelands in Phoenicia. He had several sisters whose names are unknown, and two brothers, Hasdrubal and Mago. His brothers-in-law were Hasdrubal the Fair and the Numidian king Naravas. He was still a child when his sisters married, and his brothers-in-law were close associates during his father's struggles in the Mercenary War and the Punic conquest of the Iberian Peninsula. After Carthage's defeat in the First Punic War, Hamilcar set out to improve his family's and Carthage's fortunes. With that in mind and supported by Gades, Hamilcar began the subjugation of the tribes of the Iberian Peninsula. Carthage at the time was in such a poor state that it lacked a navy able to transport his army; instead, Hamilcar had to march his forces across Numidia towards the Pillars of Hercules and then cross the Strait of Gibraltar. According to Polybius, Hannibal much later said that when he came upon his father and begged to go with him, Hamilcar agreed and demanded that he swear that as long as he lived he would never be a friend of Rome. There is even an account of him at a very young age (9 years old) begging his father to take him to an overseas war. In the story, Hannibal's father took him up and brought him to a sacrificial chamber. Hamilcar held Hannibal over the fire roaring in the chamber and made him swear that he would never be a friend of Rome. Other sources report that Hannibal told his father, 'I swear so soon as age will permit...I will use fire and steel to arrest the destiny of Rome.' According to the tradition, Hannibal's oath took place in the town of Peñíscola, today part of the Valencian Community, Spain.")
# s5 = model("Harland Sanders was born in 1890 and raised on a farm outside Henryville, Indiana (near Louisville, Kentucky). When Sanders was 5 years old, his father died, forcing his mother to work at a canning plant. This left Sanders, as the eldest son, to care for his two younger siblings. After he reached 7 years of age, his mother taught him how to cook. After leaving the family home at the age of 13, Sanders passed through several professions with mixed success. In 1930, Sanders took over a Shell filling station on US Route 25 just outside North Corbin, Kentucky, a small town on the edge of the Appalachian Mountains. It was here that he first served to travelers the recipes that he had learned as a child: fried chicken and other dishes such as steaks and country ham. After four years of serving from his own dining room table, Sanders purchased the larger filling station on the other side of the road and expanded to six tables. By 1936, this had proven successful enough for Sanders to be given the honorary title of Kentucky Colonel by Governor Ruby Laffoon. In 1937 he expanded his restaurant to 142 seats and added a motel he purchased across the street, naming it Sanders Court & Café.")
s5 = model("Harland Sanders was born in 1890 and raised on a farm outside Henryville, Indiana (near Louisville, Kentucky).")
# s2 = model("engine engine engine engine engine engine engine engine engine engine engine")
# 2 - .25 1/4, 3 - 0.33 2/6, 4 - 0.375 3/8, 5 - 0.4 4/10
s6 = model("She is such a nice pet.")
# s2 = model("Diesel engine diesel engine diesel engine")
# s2 = model("The engine is galvanized.")
# s2 = model("The car's chasis is made of aluminum.")


# s1 = model("Alexander")
# s2 = model("Alexander")


# print(how_similar(s1,s2))
# print(how_similar(s1,s3))
# print(how_similar(s1,s4))
# print(how_similar(s1,s5))
# print(how_similar(s1,s6))
# print(s1.similarity(s2))
print(s1.similarity(s3))
print(s1.similarity(s4))
print(s1.similarity(s5))
print(s1.similarity(s6))

# # print(coherence(s1))
# print(coherence(s2))

    





