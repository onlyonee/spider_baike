#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write(
            "<table border=\"1\" width=\"100%\" table-layout=\"fixed\" cellpadding=\"0\" cellspacing=\"0\" style=\"word-break:  break-all;\">")
        fout.write("<caption><b>抓取到的词条内容</b></caption>")
        fout.write(
            "<tr style=\"color:green;\"><th width=\"10%\">URL</th><th width=\"10%\"> title </th ><th width=\"80%\"> summary </th ></tr >")
        for data in self.datas:
            fout.write("<tr>")
            fout.write(
                "<td><a href=\" %s \">%s</a></td>" %
                (data['url'], data['url']))
            fout.write(
                "<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
