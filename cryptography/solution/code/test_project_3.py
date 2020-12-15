import unittest

import project_3


class TestProject3(unittest.TestCase):

    def setUp(self):
        self.project_3 = project_3.Project3()

    def test_task_1(self):
        m = self.project_3.task_1('0xbd2b22e48241fa4a85bfcdc240f74217ac37d40cd34cd55065af7259c4317f7da5a8c918935f04f00f0710dd9cd947e3d2a2ce1ca969d8b217f737ec549934d40af35614da4a7e2e3d2d329d408cacd21a80038c49c232935926419d1de2658525bb83493e05fdbff6eb1b99d5ef4cab2666e1cff9d0d4c3895871036453ba91',
                                  '0xaf17623087b071eed0657c19b4f027a8a9aaf306fbfd3de4307a782946435a71fe07803ad30d3c10c6980fb050217d3d0e15cb191465f840bf95ff992ba4b31389300053fd3236188286bd4a343fb70273c18cb378e120b7e44e2b9028d1267d4f6abf4bb31744ca480c0585455cf7d207e04630a3bc013c5bb8ff4066c41801',
                                  '0x7ee9127facd9381ceac3abcc4e5b6109eced930a683aa465e8b8dcc46b2b2ea78b3f4142d40a57cb6536700b04ebedc1817de38845b700c249def436c21da3538e56955f694ff02616138f05dde077cf6f18be27ad84ce4576e3e4c5691c0f6cb46f5519e007f0be70cec37fbec652b52c881c3a3d19e5857b92ba6e772442f')
        self.assertEqual(m, '0x74aeb7579d4061e3ba54f02b2eea47c1')

    def test_task_2(self):
        password = self.project_3.task_2('0bcf62b62f026b799d6245fc98591b58f6428db3a828303791f135360461d4ca')
        self.assertEqual(password, 'bryan')

    def test_task_3(self):
        nonce = self.project_3.task_3('dolores', 'satoshi', 4590387, 'ad1a53f6aeacaafa9a66a7c33cb336c7c6a866467883960ad5731db2d6aeae8c')
        self.assertEqual(nonce, 656)

    def test_task_4(self):
        d = self.project_3.task_4('0xcd6290ea76c25b9', '0x10001')
        self.assertEqual(d, '0x15abb7c3f3f39ad')

    def test_task_5(self):
        public_key_list = [
            102030335122870868590017335061536003286114567515694190846922425692939581397137799771148042645209053266408856676020488471542642894968721317584483648375331386225206894437503042773785583693545539295872067070407007231395761593648259319513478714194949429200107481027864208788092576669132665180811372548044760729527,
            150715631773237262076472147988245322719644331923332947474936899130743246195039636399473864468439280962228740175701427878219200091303113220680313018921285409551087936322585648640437112044394828249340159427668659622146390972467568882398644429594851384175273765319397145042811245981386060910740060095224464610911,
            153632760614594955484679058385978384656033681481738918794841722380008205340288157234912446400924825738075492687377261037833256664346391454130781703693091261399554497056672166503473502426357703130277412794172699397683377989068599450443408130457761568074872983548850223762132720486551390886265116150311248202531,
            124738289224343949110561421815812968569665065704452196771322956128975578299529502085935593756529018483577740506147461336743008745037325297852025684495015214944606546582218520727944803661559848461430786599990780549264056302867136209004622971165029190902588224022405900046926623654930282607923625554281253648241,
            133826960967158225326417090806907721903474590026193317808007153898665547579406276317135972454779921328579835626245555546001259211869871125607207981501099988954302150435106498224365763753516151994779912364327138934357759815069728219163444662301995598587079828462389419002878030294287989831716317444579002020217,
            152200101632053843682895386859228689153759559144119975461317904845583667423548174353040616163025468545410367658266666980531078930711728940420554370492847666860261784066886447023472081884008522801829235366070273243068818202421449713282247785462798683472297347367000082590241107602693279292334395101128230270889,
            140579023745795349438596151547419357651909033388154323479959207557113939152063267329510023532650266621954903972892872193963047647988918521467395023121681437409186441331126437179877484975116675355491694438357400002930556879732008767608151745054760880743219021490527042046754558682864547512337189438055793792331,
            141511127252365398074592785989716354074051765434528614540071183020123232112420438000259412845968835682565154769011017757707435483432607386658978142738718287363535582000645766679271611442507411747220534034591587089673728315034358912632138813070711523898711289257505297099105443313949213261727745958214638193133,
            150548132051915712222483002258859868172772937411082925828692667749923626149608936362193744786757845221541341848132308446373194667668055705933172322732363791929521422983522929779243650843702445940213010000350237775865796357063534145708889484694069171451557662404718236514016421354525351435751378190027655612819,
            165415541979697985885662996967511863794689940082459072143124545568279122476941013053515290884607030846499817672179286755612472722835618692597439675419366414551418634573988066161081914057415391180488600386992999023141483951596067758010150629882976829614354434375017423863824749028119189957269100192927874615009,
            120647291017266915984333778634887094389950233221113222690820909137510260551178417501019500857627930833440141210922452308346246051804349829408942336547836659837265455235045157767951747971117794080664681211312686247648260896871357908047906446532366524132545870424783614913725432822996773955683023369808206352847,
            171598451220367942156369502170981306605071722291586876180506839254408475396091585197764843037504922929204649205228608201678688636693052697872832592834675087162632465451626918067944933217430496376535222661471610266116472755990266699342627664050857819063330384171193184407154224072054589043870340129940532991021,
            131901065622509419949105145910325887079255093424498128694452187790583758493716480613685064997523991906009051299587096290808701841400796465178962126545235022901784639192265369769503462440997937183298713364249732213710562407298663842340774667407659685254385819202604948097429532037521498771066566336364076648113,
            96563755417810568791227258477562363399219473761801998937491379388534857564772643950208937782255870055152616078385195140078752088972363909006929746167361335457164651588020093787258089404600845691354068029371667336563233497798973221364029093053923278277354505800286531404363674312697897544287362300375251220859,
            100340241292801088792453531376653444760061026875447792422199201096636833164676607024907371584759004410380248615440843448846058220112686772283082393642226660168262915487889940391526279205864050477397657724758272223638050633850714932586781124302783236685756217712418626907567953945783097758046473729504383807297,
            118985169760967373594755184295656597642461932685355594204636287835263705537096001066176201287189502219820193955796707020769436060308653737212332057779849439040199650488312035072363117678334728805923611438272301505436765152690480648750926140403399736240780863541182374081442213469076434190108894213257230644993,
            102163818327283382865197002112069136940631722040488122025447770231155309095823132697827981225183362179222234953126333737817170792080936903699577916637451044781996042200201386534244320100046236956431206978262473644350138602754031959098207115970855407440407407870035450680488640100938617968934961297422761200543,
            109321532717336735261040346471506719017566429638571609404955425846397400753394932150094146482041945562057085738291138274800292610742022401362064135744777788092075327584810434995774587736203785058471026479520722579167655149968571409435925802537641406525820683229580069790813610974892038834977396574754212288981,
            141023567093241828150913977171821952662358576342226015482229784478633230318231244581296869359288917258581903123650861829700615581698419061069754257962786119572932017839185357205462672617539445142292276719912635201931142994912583379141371058406954674306464754680937571881393028368863639496295009727289005958613,
            154698004670264224347301016641989858750377643726359066169828989468760154051506088164555935271792517481451928662814352646996238089950486773180714087492824628602715910370537648831774865465560356736675931662927484705952692105937406901673395771219258641006145105330942078645135578123345470039327583802298599606387,
            155367604808315095109839423110305814002157945354093015764837941244452545379472498645177298353479553341441759375495508406696289628242544640422166914703797558967674880734936248432087412968957295020295937911847502754458927980344616853092684925367628725227220541848654097270774619584973000630350770933245251794833,
            111900712648326243077199034592491121222644402866536072894117963574643455550481449236228426152554353821029589524198920363581568209768186299250627833742555742235577149912319917318749459902075160437175653246367352351393932866258343323340457554677514143238371082747685168544256792318387380820716709144751857342707,
            113627329439711958563013467743931124241366692233993956789639551197486337433060867317415932860230017597399909238235135333464863585851886642708400972953486117235077476631704884744292952485767219304522031757304625288958697990154080487292361152824685228202112481928921698292503200973859437213997725261261674306049,
            101117530401441258287062062104531362864004752875814941607145945331722623339574331910928542014503540503471456076504989198270701629125875765316133766920257342547456251447794361881120700070192938794317144521011535988275713913386115989038781946083592766494864212447025112240348940252601851959350332474514625412761,
            121303632021663348437545373506914230273553155589312837434241040387134619100977734869112634517974924622706261061413404642972893729759659087792234395816874370430322752014081385537343960525310819167266012359767987887537433933159910725253714639959283757070137670015573474553712576738033244042191474135628002517911,
            133901865833651204510034843170109550155352947637071117817479149167670617599041540271841230668275602196936900919072220540531231989093362850719696193373474489227183284476821434928419058305553395355283677619327503691737488993840103946600819791250087844140587629608906932943059289181767196609912009917235409015897,
            115713097617978672128981286803657283769973082314847592351311659214421962661928561375801726937932304896002414708965769917815075293911420563233116334175416363397632058123174002898164261490535753535954812652829780241384080792689522730250306841304195408504381311994996320946296662144630952217182909527309942397259,
            149249838727785896057517027403037872506902430639818532109511042474474376045194766005607787203470159178473533419564607834523562143946602047190521706541596563680401140217215330058088393837712798666628192051193322268760429992249796732628483842409871890129837700793196286119473201752448823842545042362854696073129,
            121662298576817860041570933725413131536372384151311417280421069307916355780775726197403058612584478010490513109340182185765011501311636582449322284932222955139274010805109095907436595317062158416758595327264917330075333123996063237689725974429861752293930784954779176251539649556713049535356045459112026304933,
            120776541672942028569954566496806543205186748944196434039118919356206729099512383669313078331452192571747646450634486063369269802971920950767756871975901473243009885383840302274016442949670555348461743456412915004436535663184151961338679325205356260819966805369197856295006952410266005821001749755907631841593,
            113199353527909408229926586446109484458162062052727268550734055262864124224531628402847387661540913046309464861621090865803935689289196036117628695451131000408420475923993957929226252185537582079263992302172443900416481444063391548048844932645101870922554396398923290955017746539684405521603347462025617565677,
            139850443483131658762036937255674717138367215579449341859601969170434700828546086938164448407386875855994406646944215999652634481794808822891992484551450510490033751047503401736401385316190907920474194559231099206781873747056276151587521929804931112615540153878554884416215773471447569657509473903629224118319,
            137041195697183195139375233739349126443855985918418393365451518760059217135549232641629471099439829875584456496858335387378943315717041293479147777215757935473234518081924454974356129970263954578155735458763243159206479216876476222979783065813758861101351950255644805150271366711240407341048485362559517332443,
            130356047911487758214049715274706576142737767314722417878941059702544803056951492037405438459169909249564339365325440740758352545259011617730780295263077385372571143289299581513104931840962949876854679003208300213967006917657174447739023463370740732421211138388247324613451448535168973514194093308086996108847,
            145357038347348291377119812068141331499823366133546920598667516886001740419288644686437304835344421796917519934389451931082226634465286043039884580723890263440725538069661287967085459151713738330041829886796783425805814288478987576123849672295562318532849028039418162581418251379021587520014474143110020895309,
            127982795192004126553854809090848859830021142574255510807432435086558392170380822109838727639005190517062860601522455392375632270744107218938057720419821095218367372519280570857171692748377199644780694037201683669474005498794745829967477825189717980530226642596310745218600090238037656463177173715911179345513,
            134665166924368629957766974606497030180095390305040177707898740249461364074409595668931586736242566398171939027967598744913772601464956680680457728218180156244021799320511450740654693689067134027683547603451417265299555140952269874811590508192980391718739596657173870728138953924625638945336285319866415145183,
            140021877456883220849890683184745427845490177734654076634982102751298189422195284395298393206746803771223084844303524976088050052040099853736448672184259540997506784698921721837977457545664046255812764370147972589138958146356782463105367949164343236515242978292749019729977751171312784996034136697701528088217,
            138007272248613269555202564151155285708094420185529988629568147671446759660636243561414419166350315636811912469582993431371956649767669435246464040440510997723722419029153181161408142311717074469112440275964683679368716474930342318044473204527420307273014003958690457703638217194222513882048279981369594498867,
            131476247007630851138307205732401896897989298000866231434422092620713631834490794036880254703340795792585387607417954813204801885155785266234836999968073024891232784327252319942763718219244574516001144601708650021605366467687609754450762552336290036422843761409567425107011500898593574898060317835375989835803,
            130689895014619148007849257037511815927135706922546975160320256872977826932499777945528757962992970441546421703135803824418104178916538838020340521338439418021626648156465225192952704819714413224643464435540487842680585623727896963650213342560539549586842721976225215014565930828982160362190293739827982167823,
            159408853257318342819285328292816557291085817767445322048526396841354804286134936026051637761177972320116983172652521626611316807366879267633230102195052553109104154415506776684660757141180132948179839455667181291075231376970867357038186722364087255682343487845143565140176178547029921242444209900621103249391,
            115587141426533700262480934668843042488389051114145996921571353749005142578515812966520599730943774408287263718789507964560968372221869482513568398574310261603571772110480938307663758021486270078803431125932755121969346759126306742652674996465466137824229507949343459131196610272171798218918790011072677626973,
            127141153723172357886705459922754573932206189684688364651280234964948842945901136221199270132946671936071600844975413474598601926995387462872427014367576812142992919894286108258283911534878808057597880711156473720046487600201492457938700025203412433278539132524756132971729959455067926837122622884726712475393,
            143059899606151672706332073379651960498174778952998611791976428880367126446299856760614562201940215769301192219083149856360514072738247292851405144241123573543296270855876496036368360569739967449604701475067775594940488760439516123854271218903011058112319078467757210863932684201622903173986407043444577710381,
            141199951924211401062893919074261001856811327472494089709980868600780920806047722881396308451537080376378793211638816790463377427794925335065067562187524769992223325574604860500604763321552821013964532078292233360277112445142192967869040571071346627623296082140958426876980778261870486539975704145460513364299,
            124028934358545421314271087403503735732935515180131139089676497973798469703540737104067929951927000210231820871366885954491070663653200399125256595191373561756269426146891441922424023790008659241370019553900294235278466456374769455349130567237393273956119281344926384921129798952352846938517890858546587564153,
            138953733224810274907910240996455702472012730656832354128043323428134390286968141778582787212251386335823444226490534516794306836168701039906476754880634807674869727650804863444383595953094862745435489740866679687763276735911986346270228995433808766665901320363821822940694006110611465971084226625189476455397,
            137843081533961298209706978810824926069850254550245778299230299258415470609185728053980758325638526072729927330442409906012501506713962586702358345090464726344969030497559702235070040205694158105636057771549238277527574674440005473503420589321319117906114448440610135325840765744958365205150575990980512330253,
            136139102277619533333385232673848899690155545239727310524398989486230245796351343545411788393240568689150690773159547466544602979172953559194454013736019942920924302949956734645476502834825039674782481947677723806798983428538611994023883164315200606121816344425719802111397747608201909586343484823012017842483,
            125699148905529569822565581803929710246268716477303077922920591576982904563368533167722473340252873828272141773159892091526106419375399572905032771941659103694487621539261172237360233684051256857898482614413067945627004345485901731601372613630181832243262399848105301147906824937268718422227222735458866901003,
            160283114645813414438427004242533374776323740076369611344690329169271522354023212999883474790611192895099256272043706945289162000167468733764730607859258225895376016563716347005010437926112788874944852140227699888964988500057867819781995647017083679057105765873028632407989031221630542968580350906936056169793,
            127058691203093221340141890637433566713295685933156417647472787325337192656917897753373912546549494105481580720067593912626425626159695467058302428786270514619903954430836447382883195895236604348773214003113703699803265800472327480777793706293696608257949549114512458824238286971790719733252945142731014110279,
            120993036477385901742433330005578204084915565074414395034519434888951279342041219372024883577567409172777499165282885630669461543678817033620299892446994693275482260126244148210118233132922346046714172053671958753490075250587059456105066989473990501245150471150583295175334095619108655606270654630365600920091,
            134848021484927832377059874720860175552657451482470469152221260108887303856010806761208340917354469670860705224193858614188521800996231520573647938618954333601956874387673261828277587839759382294285573533519895252247367245021273144172637778070028226464207943903039404766905093730125404121205620017750815327871,
            116043440986230300666685996928324694270981452303055101082039719428330918552083046439040521621211086710593456742097304803903621465326322486923306842344024385208661231520304809848110217768757353841706403062385183090365899138104784543012991319047030518516821699589251441594492903087559923988577369163931482383799,
            126514207184925510500934517223690776653848805094423056326992579900775975671221739207129269550659493692821205889895255080324703886169464471735469374128414727321389862431053938547737485244816692651174917682092317543168415051224325987023931007276735575008533343409939603909103890685388872805961859005424655977819,
            102785597248347942868278389044457543389930519396233011290239691495679884845100967385447671683232811140223040142138980913183847220490984588188316718931556832096398766969092160268549231344931185448343133483773598570729366486792956500148365220679023119450629287715549478249042272021522718760795595175753302850091,
            142428519070963172603974043611205052580023830127763998229321981981485171756641632074909726840065391305904799892996753941651242004514140724608759321539447369168967133372866229973740509819936267145020331951871961696312340249597606412219953862513791839412198210485093134950778457843002490562763342094194778192187,
            112737944458362546804615829508464698692584165539888746941783594750145464074885423613548964079116420748807489842283748837492236174634748728064462053315536043347924416255137795830340526133843704377525481299692801586967125767991507470989841047333110143044886789416035343340510466943499043720169927947087111039419,
            130612033712392011457074883720616470124012233810840424829813505499345647033362530005072667429713777945181205094443133330901773689387024480973085743530313053809622906514501012193215433579768489113014545066737437419240293689638097022524485908007946262218499697790675397830376692448857526518709576865461189661363,
            135607775961545182282860222929689502202394272486076032626771523658417407501015649822041847658504943770772029605432366165219797092334316713955005255540932823889145039948221221853309399461219004376641800778837089277018079617859980904357414229728332050405801099458325763716091087861555187699971349771050441031239,
            113299982791746127385544432491708648381253564237858623871338889381674417176591509159186680653698677032890561608491580183289213210781549559445093695334910698278859815097740350081586435582456682091306505859771956405440830052388989264031184604737890573304915753642803815077648237500989505203351159047224268973067,
            161478187205405270226398820970270185844683972434253509259957562772921088802333168912613997063606160108983675948968276302607768885010784566776112661462346190712726837948514151515958693897241492692747277320370575032479309858288156100159067959406592701021379393614311255003150040408638320736139681486645722790379,
            160484970550794136846284123781698806092075428100849942252680225595038591959037730530204222492106721665729873223192115167227747169287430184530045134345182074835201064133464013006698462555899995168339665288887256599362365117665631839424061844195476757070073679617653767408592374600098168533557675763016390776921,
            139105165711491838378701009490848103748955154252485945582137426298500712794189788409254832410030149895291310382257111089986575908614774669976606227569228713786939853218518653278038891643440162251798932767717736447360783359860394479174884900371329216245464549355987831202239531842005209685418775443332863959637,
            142852635209994537869340239734173625148479319740450563804853638786067360366023160402794984149995762413722442360893200780386533018014224468951410828526203254462280192178150827489412046297828082074189074713161349778353903616776690217887892802251167975663042601764398310131635208986136638182535375484891049260307,
            164754370520103881052457294757866591154132981066258304680341240424238381882607827704504678625574179461741927319337359653854363321388058003807488730127218218255162164896276980862864813121710203973524755297053409176273303707237250200286167149117820694492241316100330060736208245913686871930898744823991005805507,
            131942882222318444758205095840826418329487457991788396987461091976323753427446901427110751594549119724999261446112538344975429179052914107959196659725491031014826233873209604967432109535392708899884828714197800533659939513707330861291069031058312636473519230484037860461645971494611280406048257132369534627647,
            109403696512352426805302814596661650100223074862166243102912056680319351887399352018370890082051106145380273858193764669956616594934819110515619400682720867181045882201573692783449982030651600717617579938064043838689435842335752532474555037419395759938833117557416555562750726539523603100620980418005314283691,
            130357981048664671292501206630961243535389294306649069508849314450234115011214305713442940649416478373481415187455619003568893910721964461748903879263586318736394473991406143449453306666573900402499330433836655061365926420397355875223922768884032515616285727372760125825370947008580473852730528916470847216981,
            137900852614755647195869472211040367305093309353364580092661816319367400267969208943730326634950716848675523734313785883416093327089344819981106300456249029245976297127818176081701555513482125674425342120232629020282694350628864086513186791765048644290847415908838285104004201108247840591884636281974581059173,
            126587656315407988468982841381025831993760330572824509021489428197534638178639934406529183174807914803437125773427087879498996450139237175051182736890067700615255817484562023865149083619678671892710615055857914461723307061719828443374214501390775111005191951059732915020176227227663888191437318388836817704441,
            132621497064537647273424964091900730152379336651546851470202751647317972239855990117642826351958116337599846400844881856720252679879030648496981924356535705255645628655443682869877177784481455566407581620576604592955139449550870529965919358198289413907734501092891699052372269532429584816445384275742099149907,
            164230903178682798639689876231059318201676403782610270668086288049818798797198076971919964689724065461134256169177301784113851188178024412846327865169844385491564750276944411001149783071813958793005525472503798680341953168607368013663077109321003157553859444536506550035547910148451417819726448148817792858823,
            107709837227112949150708032602971605639027900820420474404441504411318832415049393625395405832657252757167695939960538556015967768575611914431368008985739900565752421857152139994420814388705023447883599145971052236355156336914205217814413833100431749320999411886261979489030689541047157935196457051579016591393,
            149623454752546039927460714348990900453590089683778877983826196018366194725074400060746038553665786139203645326293824738292837089618683725856735302294451974283986695667527860469836567090622083715434051878000787942025382077882630938716406943303387306247810602469512853077936235281583817171912981675971446118591,
            127031986641892436586710355950973229853035188153816394049589982521339378131035758939662929349132126970110953784873881770536475091530751452325833212930063729205076928235482696317750534557580907119456113773777522511194022729131018454667885601064137084897370645722730341932761057817924349615604054089431086910249,
            126409694910200570389824236246367263703704743850513984570044799800106872432179613804718615683393935745750179916603480880128369485680839363825036019455247330078983667162200979999488720396438826077506094123971237341970221714041035577467460174544587272735694755590397130104687788366500696454950966662801357231671,
            104242378855544607414397746747360652120140423849675512403000748794160226840711104406933144352734419861914831284656158837810375051549577788789976791443827426753849077723798361582913396586452094213833544953993742369481267144099236574233333261250463297044810397386510024892527645718122052762284480470092320710731,
            143882162601106214667170740253092635849120965986472097698959297237813640075869189772905158190529813314383966047091933720953312881466882811974863264090441170944274661998897934600754818342304853589739730968256068357719873944387703324427970261996979702030967336604373877525690564686228264547434338455541286225057,
            151505762690248374359306895808498408033037488852893667290635604430126801266202311302999879643920952752694188712581939028392705125608802489721059737603420831069038904540966747826834261355243851402490839567150278429149855558623124562798349513056267334940729061480461561064712880696195215310478312131567681281447,
            169587118327600728604960013929660975271539489730446167818393710519747486983883369883242928598406541553256811826673609171905050096511148435837539749602150774137293426577551903521281718554990516739805076965558373876146733077013312411563164654129893982172259877886930972713460315193019543750517696115838596779077,
            124382061116233858828496713429952633106400774299327907582182931826023028366011600567991041958791604984549372804240073696939913411708576183272765838550817229814370048485886266632963671032535874287425661239925731129537107622502147170552692237255966546973326201652467114250726054028109378637957329123370399127803,
            166755561198919746385781828945896658076785671690897197211684299579204575220196398987071359913276090568536073833592889460506703132421940667208808860867793549060846563323147549739368339295711611535344695676998336265520300813654872442563638763051865406758467700209045330134141590296064131733061818062053096280051,
            118764128733590436068137303170864607522134754365445489758245775513934939379889372561693491683815509502856971054948453609379008718572634853311265676330712944794447453706703059521126350616987350418080953093484590008787759252657426003801328886533302324772655486171705085411719096648561153716988575925870173949473,
            135719831628949080227997710832801475104554952596758047433113047083156477215614565609455824288593395820687047356785516151945289213295359916616871443572146597554804676561499962304699284155925462072502317553464339911941453762874441263201692526691697247711783548601325755245249373386362052493999490161487399457537,
            122477617449514630324186166426931074629521925795751538438606324557418083578419042061507201356329334454448189972236411786145552808081179490640111739236665424369103071933009388415008435599698796556301921864425957644792569818857379775711091237908712287991463674770414124429779050743712543354034939570377614464349,
            141075229553221249332349124000352395682792505766330676097109386294620720787953035460655338748786158718732077783673001219856743423690725896603088147208659303145134586853379721348448974586547960636817036825460042993956717509303720291871827037159729490057291808099566297429407365676507055798822572652209200347851,
            101947320750571607688797531183042461864965051456443196896487732219871302429247794904538744213517818614391167663815135299698506953200800014121989351208260639773701175614474483752972230434788387718390068580300225895263877529760260889521369506597492871069839303459109289867601381649503595366709665294709535793447,
            125592329857308843774072047429298485182597379449436323426669566683213742968910080081396023588094195118827600954499890240050155135356572964013376484039262789715975255662498323892430754813652657886209612668559845288500434144802860906018397061235858619617054221693905329713224073345563930428944236242580961154761,
            128325316073108547304953194093584487249555222247248648317013771663114024868634952852605126347532865665298649989718250294042295575507992578385508635165317188817714338483796723435696662346693525355316575999186684917831077690027983745474506637684663182298658919197473383046521624986097129619804194384212693503643,
            142864269423940498969167561923463076881858326067365043815017473196407564426464535925885540576698324461764938778910362274690212335860736387411372668313000512370342886311293653446969683095445811684124798196901400148668019795865715664647274434582502963176561820420943746413854827515754255698352909159256895376581,
            100604201513430856388583646989804216561771273406381692220346809670566933910051415562879254215920991713148695825475826043127761442263635096528378244767646133526796342400950352794044941432228969391550143445941570343812253230465134398392504523794167191881658677422111362757576826571890997012077203841350159072633,
            98617787126818012973377542391993006823011878265519217366866479830874572403257788192634918255050126040372005418544759504683126998599064578049658435519856925845568591055680611385737975568788368267008459600590530752438882681265319126320059099212201429551435511801416433213448132482548641277860119900939515661023,
            125610791461748955638616102148131081324921236072171511319411466618889364674230112548040896597849146112750536220872902582969456610613684837357203534819826868317678244892292816398611078039287827050406711931037842789191545710393195373695650928156035666392310247688814169018791141426648784629132853579021869448087,
            96943741031608309026979834116895796566918868780178907580473083514935405882352488181378045464755980057257093244793343189140412050317111136678535803897016718868351472132482643536414403372848418724182514118180650785652629591546129008822934700927660579558186301264593377170492231586852739746255105776079417885793,
            138943111746232182913476518507343890272759802153516130508570913058061183682776226834174216784132778199936584590403988878751915340008216505000134027525460631262301100315227147890869529579427469194808877169527028641786625708626205329018898097424797630708637959097469021080701528672411727981115786125662531591639,
            109811890252645932088283226521986041933636827231368825720561133849854061837149406418749559599567436785557562683019036723095741502558157358527906065490867320305858687237071062844483603860062831765216112888908238744963577160904483246867698821816670195963049614238857851266529657953159681627183009455016117186269,
            137757283028252517172062934464414672793209839622790795071654548796274701685632321050646282359943779266404556814688834477491606876449911506487963931320162030731849319523678048484988375227818763243101948855350024495050232104819414277321538652713421926569273382050274845348734362127779392649258919470254073172183
        ]

        d = self.project_3.task_5(144965985551789672595298753480434206198100243703843869912732139769072770813192027176664780173715597401753521552885189279272665054124083640424760144394629798590902883058370807005114592169348977123961322905036962506399782515793487504942876237605818689905761084423626547637902556832944887103223814087385426838463,
                                         65537, public_key_list)
        self.assertEqual(d, 74802245043332336819738742183008736301648777657397930159129389056116909388432714085680956881372970342479802834336610553689728155626808313902743699024874423336538299682452950217808789958403343592531615457200132930152958054550525183117023557696239548759739686054789111129430445374962073993156006641973866251561)

    def test_task_6(self):
        msg = self.project_3.task_6('0xefe95570001fa9c8f2c7380494ea983516378b4f8c550ee631474a0074adcb2fc472e00b5ac60e87468a0ab85d32bf5a023e96dc22d8dd39a343c4105a6091b5a40b09f22c2d3fdef2b7ddabf95277e40667114d0b134f92339f7ed68ce6ae71da3dc7e964f789a06193d6e919efe1f8f057e58b563cfda790c0c89c30cf7b3d',
                                    '0x2e6f39b2c3a86519ce78b92bd6843ac5030900ea5ee9bea55d9476833dc315d284e523ed70e2663d8749748aca551f0cc8f404722d81de2412766a61c5c6665b9ca1874065f052d01ff94f69b878d18d5d1c2cd6d1951d2725e15e00c7f186492f4e79c43261df3609d1d3d17c203e0f7edf3ceda097493be9cd2bea35d1b8ca',
                                    '0xafcd249a366d383e4f17e1e4042df707200cb0f827bb3e21f6e9b6421a6690933ca474cc54bba7bdf63de955beecae111a590ef3e12ee5e7ffcd2f1fdbd5b345a6b15b5b684a80628153b50b6207441084d0488068a113c5f0f897b6d4d9248e551af59d637b15ef650bb76fd15b4b85319029c43a4d88475babbcb4f6ec492b',
                                    '0x98a6999519c83bf76bc92ffb1926a0f4b82f1b0e64551cfe0f5105d7933541e2f99201efca6f22fe1f3a538511eb4123b897d603f0c327113f3f8d62672ee5c845c02e290007732eb9ebb9567185a8f8a2a83fe8144fcaffb678ab791f5cf98b57bd76ccd1b26347e5c163993f569b3bf66b3c6fd5fabf503e939aff851b0007',
                                    '0xa2e6fd084a7a44073a5601f492a7e2c718e03cab78735b239ef988eae4acbdc7f4cbc23a13f653c50d7950f9ba60675ee345ed400997bdc9dcf75cff9e1de4bc0de2345e66f58f7ea95db718eafc2b80f7641da266c6b7b49b67ddfb1abc7e4f53e384383a8490242bedb55f2aa237224acacc7160222ed16db52ea875f2e0b3',
                                    '0x56d43b9f91e6fcad96c25a577f55b35c5485a926bfdd8d42f9e8251cd5f904edce196318a4c93927e203819d2996223883c0a3686acd1c8fcf81771bc260a408f7f3c3fbf19a1f013f7c03bdb613eea23ce8ed347ff04174cd1b6ab790ac0c1f3559ab9100e6d9b88a1960157d8c4cb4a0df0f1fa69e9c24ad15c0b0e028244e')
        self.assertEqual(msg, 'They are the egg men. I am the walrus. Goo goo g\'joob.')


if __name__ == '__main__':
    unittest.main()
