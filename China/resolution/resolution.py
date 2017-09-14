#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 04/09/17

from collections import Counter

# Aislamiento de thread problemático (ver archivo top.txt): CPU use 93,3%
print hex(16994)
# res: 0x4262


'''
1) Aislamiento de excepcion:

"http-nio-8080-exec-30" #59 daemon prio=5 os_prio=0 tid=0x00007f0ab8bfa800 nid=0x4262 runnable [0x00007f0ac11cd000]
   java.lang.Thread.State: RUNNABLE
	at java.lang.Thread.isAlive(Native Method)
	at org.apache.log4j.AsyncAppender.append(AsyncAppender.java:144)
	at org.apache.log4j.AppenderSkeleton.doAppend(AppenderSkeleton.java:251)
	- locked <0x00000006c7595d80> (a org.apache.log4j.AsyncAppender)
	at org.apache.log4j.helpers.AppenderAttachableImpl.appendLoopOnAppenders(AppenderAttachableImpl.java:66)
	at org.apache.log4j.Category.callAppenders(Category.java:206)
	- locked <0x00000006c7595c78> (a org.apache.log4j.Logger)
	at org.apache.log4j.Category.forcedLog(Category.java:391)
	at org.apache.log4j.Category.error(Category.java:305)
	at com.mercadolibre.furytestapp.router.Router.lambda$init$4(Router.java:71)
	at com.mercadolibre.furytestapp.router.Router$$Lambda$9/1404963349.handle(Unknown Source)
	at spark.RouteImpl$1.handle(RouteImpl.java:61)
	at spark.http.matching.Routes.execute(Routes.java:61)
	at spark.http.matching.MatcherFilter.doFilter(MatcherFilter.java:130)
	at spark.servlet.SparkFilter.doFilter(SparkFilter.java:173)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:192)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:165)
	at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:198)
	at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:108)
	at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:472)
	at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:140)
	at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:79)
	at org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:620)
	at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:87)
	at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:349)
	at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:784)
	at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:66)
	at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:802)
	at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1410)
	at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
	- locked <0x00000006c95e6a08> (a org.apache.tomcat.util.net.NioEndpoint$NioSocketWrapper)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
	at java.lang.Thread.run(Thread.java:745)

2) Buscar exception en DUMP de Memory con VisualVM (o herramienta similar)
	Ir a spark.response
		Expandir response
			Expandir request
				Expandir requestDispatcherPath
					Buscar strValue: /items/bye-bye

Nota: EL archivo localhost_acces_log.txt no sirve para nada D:
'''
