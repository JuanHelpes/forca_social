
from sim_ca_constants import Constants

class Logs(object):
    
    def __init__(self):
        self.individualsDistances = []

    def generateHTML(self, directory, tempoGasto, qtdIndividuos, qtdMapas):
        arquivo = open(directory+'/index.html', 'w')

        directory = ""

        arquivo.write('<!DOCTYPE HTML>\n')
        arquivo.write('<html lang="pt-br">\n')
        arquivo.write('    <head>\n')
        arquivo.write('        <meta charset="UTF-8">\n')
        arquivo.write('        <title>Relatorio Simulacao</title>\n')
        arquivo.write('        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">\n')
        arquivo.write('    </head>\n')
        arquivo.write('    <body>\n')
        arquivo.write('        <div class="container">\n')
        arquivo.write('            <div class="row">\n')
        arquivo.write('                <div class="col-md-2"></div>\n')
        arquivo.write('                    <div class="col-md-8">\n')
        arquivo.write('                        <table class="table table-striped table-hover table-condensed table-bordered table-sm">\n')
        arquivo.write('                            <thead>\n')
        arquivo.write('                                <tr>\n')
        arquivo.write('                                    <th>Indiv.</th>\n')
        arquivo.write('                                    <th>Iteracoes</th>\n')
        arquivo.write('                                    <th>#Andares</th>\n')

        arquivo.write('                                </tr>\n')
        arquivo.write('                            </thead>\n')
        arquivo.write('                        <tbody>\n')
        arquivo.write('                            <tr>\n')
        arquivo.write('                                <td>'+str(qtdIndividuos)+'</td>\n')
        arquivo.write('                                <td>'+str(tempoGasto)+'</td>\n')
        arquivo.write('                                <td>'+str(qtdMapas)+'</td>\n')

       
        arquivo.write('                            </tr>\n')
        arquivo.write('                        </tbody>\n')
        arquivo.write('                    </table>\n')
        arquivo.write('                </div>\n')
        arquivo.write('                <div class="col-md-2"></div>\n')
        arquivo.write('            </div>\n')

        #Parte para controle de javascript dos botoes
        arquivo.write('		    <div class="timers" align="center">\n')
        arquivo.write('				<button onclick="SetaMs(1)">1 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(3)">3 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(5)">5 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(10)">10 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(30)">30 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(50)">50 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(100)">100 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(300)">300 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(1000)">1000 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(3000)">3000 ms</button>\n')
        arquivo.write('				<button onclick="SetaMs(5000)">5000 ms</button>\n')
        arquivo.write('			</div>\n')
        
        arquivo.write('			<p></p>\n')
        arquivo.write('		    <div class="controls" align="center">\n')
        arquivo.write('				<button onclick="Retrocede()"> << </button>\n')
        arquivo.write('				<button onclick="Recomeca()"> PLAY </button>\n')
        arquivo.write('		    	<button onclick="Congela()"> STOP </button>\n')
        arquivo.write('		    	<button onclick="Avanca()"> >> </button>\n')
        arquivo.write('			</div>\n')




        arquivo.write('            <hr/>\n')
        arquivo.write('            <div class="row">\n')
        for i in range(qtdMapas):
            arquivo.write('                <div id="banner'+str(i)+'" class="col-md-6" align="center">\n')
            arquivo.write('                    <div id="banner_img" style="display:block">\n')
            for j in range(tempoGasto):
                arquivo.write('                        <img src="'+directory+'crowd_map/crowd_map_'+str(j)+'.png" class="img-fluid" style="display:none" id="mapa'+str(i)+"_"+str(j)+'">\n')
            arquivo.write('                    </div>\n')
            arquivo.write('                </div>\n')

        for i in range(qtdMapas):
            arquivo.write('                <div id="banner'+str(i)+'" class="col-md-6" align="center">\n')
            arquivo.write('                    <div id="banner_img" style="display:block">\n')
            for j in range(tempoGasto):
                # arquivo.write('                        <img src="imagens/Tracing'+str(i)+'_Iter'+str(j)+'.png" class="img-fluid" style="display:none" id="tracing'+str(i)+"_"+str(j)+'">\n')
                arquivo.write('                        <img src="'+directory+'dinamic_map/dinamic_map_'+str(j)+'.png" class="img-fluid" style="display:none" id="tracing'+str(i)+"_"+str(j)+'">\n')
            arquivo.write('                    </div>\n')
            arquivo.write('                </div>\n')

        for i in range(qtdMapas):
            arquivo.write('                <div id="banner'+str(i)+'" class="col-md-6" align="center">\n')
            arquivo.write('                    <div id="banner_img" style="display:block">\n')
            #static-field_Iter0
            for j in range(tempoGasto):
                iteracao = 0
                arquivo.write('                        <img src="'+directory+'cult_experiment_static-field.png" class="img-fluid" style="display:none" id="static-field'+str(i)+"_"+str(j)+'">\n')
                #arquivo.write('                        <img src="imagens/static-field_Iter'+str(iteracao)+'.png" class="img-fluid" style="display:none" id="static-field'+str(i)+"_"+str(j)+'">\n')
            arquivo.write('                    </div>\n')
            arquivo.write('                </div>\n')
        arquivo.write('            </div>\n')
        arquivo.write('            <hr/>\n')
        arquivo.write('            <div class="jumbotron" style="margin-bottom:0px">\n')
        arquivo.write('            </div>\n')
        arquivo.write('        </div>\n')
        arquivo.write('        <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>\n')
        arquivo.write('        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
        arquivo.write('        <script>\n')

        arquivo.write('''
            function SetaMs(Timer)
            {
                clearInterval(TimeHandler)
                TimeHandler = setInterval("mudaImg()", Timer);
            }

            function Congela()
            {
                ultimoinc  = incremento
                incremento = 0
            }

            function Recomeca()
            {
                incremento = ultimoinc
            }

            function Avanca()
            {
                ultimoinc  = +1
                incremento = +1
            }

            function Retrocede()
            {
                ultimoinc  = -1
                incremento = -1
            }

            function mudaImg() {
                $('#mapa0_'+indice).css("display", "none");\n''')

        arquivo.write('''                $('#tracing0_'+indice).css("display", "none");\n''')
                
        arquivo.write('''                $('#static-field0_'+indice).css("display", "none");\n''')

        arquivo.write('''
                if (incremento > 0)
                {
                    if(indice == '''+str(tempoGasto)+''') 
                    {
                        indice = -1;
                    }
                }
                else
                {
                    if(indice == 0)
                    {
                        indice = '''+str(tempoGasto)+'''
                    }					
                }

                if(incremento != 0)
                {
                       indice = indice + incremento;
                }\n''')

        arquivo.write('''                $('#mapa0_'+indice).removeAttr("style");\n''')
        arquivo.write('''                $('#tracing0_'+indice).removeAttr("style");\n''')

        arquivo.write('''
                $('#static-field0_'+indice).removeAttr("style");
            }\n''')

        arquivo.write('''
            $(document).ready(function() {
                indice = 0;
                incremento = 1
                ultimoinc = 1
                TimeHandler = setInterval("mudaImg()", 100);
            })\n''')

        arquivo.write('        </script>\n')
        arquivo.write('    </body>\n')
        arquivo.write('</html>\n')
        arquivo.close()


    def saveIterationDistances(self, individuals, static_map):
        sum = 0.0
        qtdIndividuals = 0.0
        for individual in individuals:
            if not (individual.evacuated):
                sum += static_map.map[individual.row][individual.col]
                qtdIndividuals += 1

        if qtdIndividuals == 0:
            self.individualsDistances.append(0)
            return

        self.individualsDistances.append(sum / qtdIndividuals)


    def calculateDistances(self):
        sum = 0.0
        for i in range(len(self.individualsDistances)):
            sum += self.individualsDistances[i] * i * Constants.DISTANCE_MULTIPLIER

        return sum

