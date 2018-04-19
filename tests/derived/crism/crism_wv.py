from collections import OrderedDict

crism_wv = {1:436.13, 
10:494.68, 
100:1184.85, 
101:1191.41, 
102:1197.97, 
103:1204.53, 
104:1211.09, 
105:1217.65, 
106:1224.21, 
107:1230.77, 
108:1237.33, 
109:1243.89, 
11:501.19, 
110:1250.45, 
111:1257.01, 
112:1263.57, 
113:1270.14, 
114:1276.7, 
115:1283.26, 
116:1289.83, 
117:1296.39, 
118:1302.95, 
119:1309.52, 
12:507.7, 
120:1316.08, 
121:1322.65, 
122:1329.21, 
123:1335.78, 
124:1342.34, 
125:1348.91, 
126:1355.48, 
127:1362.05, 
128:1368.61, 
129:1375.18, 
13:514.21, 
130:1381.75, 
131:1388.32, 
132:1394.89, 
133:1401.45, 
134:1408.02, 
135:1414.59, 
136:1421.16, 
137:1427.73, 
138:1434.31, 
139:1440.88, 
14:520.72, 
140:1447.45, 
141:1454.02, 
142:1460.59, 
143:1467.16, 
144:1473.74, 
145:1480.31, 
146:1486.88, 
147:1493.46, 
148:1500.03, 
149:1506.61, 
15:527.23, 
150:1513.18, 
151:1519.76, 
152:1526.33, 
153:1532.91, 
154:1539.48, 
155:1546.06, 
156:1552.64, 
157:1559.21, 
158:1565.79, 
159:1572.37, 
16:533.74, 
160:1578.95, 
161:1585.52, 
162:1592.1, 
163:1598.68, 
164:1605.26, 
165:1611.84, 
166:1618.42, 
167:1625.0, 
168:1631.58, 
169:1638.16, 
17:540.25, 
170:1644.74, 
171:1651.33, 
172:1657.91, 
173:1664.49, 
174:1671.07, 
175:1677.66, 
176:1684.24, 
177:1690.82, 
178:1697.41, 
179:1703.99, 
18:546.76, 
180:1710.58, 
181:1717.16, 
182:1723.75, 
183:1730.33, 
184:1736.92, 
185:1743.51, 
186:1750.09, 
187:1756.68, 
188:1763.27, 
189:1769.85, 
19:553.27, 
190:1776.44, 
191:1783.03, 
192:1789.62, 
193:1796.21, 
194:1802.8, 
195:1809.39, 
196:1815.98, 
197:1822.57, 
198:1829.16, 
199:1835.75, 
2:442.63, 
20:559.78, 
200:1842.34, 
201:1848.93, 
202:1855.52, 
203:1862.12, 
204:1868.71, 
205:1875.3, 
206:1881.9, 
207:1888.49, 
208:1895.08, 
209:1901.68, 
21:566.29, 
210:1908.27, 
211:1914.87, 
212:1921.46, 
213:1928.06, 
214:1934.65, 
215:1941.25, 
216:1947.85, 
217:1954.44, 
218:1961.04, 
219:1967.64, 
22:572.81, 
220:1974.24, 
221:1980.84, 
222:1987.43, 
223:1994.03, 
224:2000.63, 
225:2007.23, 
226:2013.83, 
227:2020.43, 
228:2027.03, 
229:2033.63, 
23:579.32, 
230:2040.24, 
231:2046.84, 
232:2053.44, 
233:2060.04, 
234:2066.64, 
235:2073.25, 
236:2079.85, 
237:2086.45, 
238:2093.06, 
239:2099.66, 
24:585.83, 
240:2106.27, 
241:2112.87, 
242:2119.48, 
243:2126.08, 
244:2132.69, 
245:2139.3, 
246:2145.9, 
247:2152.51, 
248:2159.12, 
249:2165.72, 
25:592.35, 
250:2172.33, 
251:2178.94, 
252:2185.55, 
253:2192.16, 
254:2198.77, 
255:2205.38, 
256:2211.99, 
257:2218.6, 
258:2225.21, 
259:2231.82, 
26:598.86, 
260:2238.43, 
261:2245.04, 
262:2251.65, 
263:2258.27, 
264:2264.88, 
265:2271.49, 
266:2278.1, 
267:2284.72, 
268:2291.33, 
269:2297.95, 
27:605.38, 
270:2304.56, 
271:2311.18, 
272:2317.79, 
273:2324.41, 
274:2331.02, 
275:2337.64, 
276:2344.26, 
277:2350.87, 
278:2357.49, 
279:2364.11, 
28:611.89, 
280:2370.72, 
281:2377.34, 
282:2383.96, 
283:2390.58, 
284:2397.2, 
285:2403.82, 
286:2410.44, 
287:2417.06, 
288:2423.68, 
289:2430.3, 
29:618.41, 
290:2436.92, 
291:2443.54, 
292:2450.17, 
293:2456.79, 
294:2463.41, 
295:2470.03, 
296:2476.66, 
297:2483.28, 
298:2489.9, 
299:2496.53, 
3:449.14, 
30:624.92, 
300:2503.12, 
301:2509.72, 
302:2516.32, 
303:2522.92, 
304:2529.51, 
305:2536.11, 
306:2542.71, 
307:2549.31, 
308:2555.91, 
309:2562.51, 
31:631.44, 
310:2569.11, 
311:2575.71, 
312:2582.31, 
313:2588.91, 
314:2595.51, 
315:2602.12, 
316:2608.72, 
317:2615.32, 
318:2621.92, 
319:2628.53, 
32:709.68, 
320:2635.13, 
321:2641.74, 
322:2648.34, 
323:2654.95, 
324:2800.35, 
325:2806.97, 
326:2813.58, 
327:2820.2, 
328:2826.81, 
329:2833.43, 
33:716.2, 
330:2840.04, 
331:2846.66, 
332:2853.28, 
333:2859.89, 
334:2866.51, 
335:2873.13, 
336:2879.75, 
337:2886.36, 
338:2892.98, 
339:2899.6, 
34:722.72, 
340:2906.22, 
341:2912.84, 
342:2919.46, 
343:2926.08, 
344:2932.7, 
345:2939.32, 
346:2945.95, 
347:2952.57, 
348:2959.19, 
349:2965.81, 
35:729.25, 
350:2972.44, 
351:2979.06, 
352:2985.68, 
353:2992.31, 
354:2998.93, 
355:3005.56, 
356:3012.18, 
357:3018.81, 
358:3025.44, 
359:3032.06, 
36:735.77, 
360:3038.69, 
361:3045.32, 
362:3051.95, 
363:3058.57, 
364:3065.2, 
365:3071.83, 
366:3078.46, 
367:3085.09, 
368:3091.72, 
369:3098.35, 
37:742.3, 
370:3104.98, 
371:3111.61, 
372:3118.25, 
373:3124.88, 
374:3131.51, 
375:3138.14, 
376:3144.78, 
377:3151.41, 
378:3158.04, 
379:3164.68, 
38:748.82, 
380:3171.31, 
381:3177.95, 
382:3184.58, 
383:3191.22, 
384:3197.85, 
385:3204.49, 
386:3211.13, 
387:3217.76, 
388:3224.4, 
389:3231.04, 
39:755.35, 
390:3237.68, 
391:3244.32, 
392:3250.96, 
393:3257.6, 
394:3264.24, 
395:3270.88, 
396:3277.52, 
397:3284.16, 
398:3290.8, 
399:3297.44, 
4:455.64, 
40:761.87, 
400:3304.08, 
401:3310.73, 
402:3317.37, 
403:3324.01, 
404:3330.66, 
405:3337.3, 
406:3343.95, 
407:3350.59, 
408:3357.24, 
409:3363.88, 
41:768.4, 
410:3370.53, 
411:3377.17, 
412:3383.82, 
413:3390.47, 
414:3397.12, 
415:3403.76, 
416:3410.41, 
417:3417.06, 
418:3423.71, 
419:3430.36, 
42:774.92, 
420:3437.01, 
421:3443.66, 
422:3450.31, 
423:3456.96, 
424:3463.61, 
425:3470.26, 
426:3476.92, 
427:3483.57, 
428:3490.22, 
429:3496.87, 
43:781.45, 
430:3503.53, 
431:3510.18, 
432:3516.84, 
433:3523.49, 
434:3530.15, 
435:3536.8, 
436:3543.46, 
437:3550.11, 
438:3556.77, 
439:3563.43, 
44:787.98, 
440:3570.08, 
441:3576.74, 
442:3583.4, 
443:3590.06, 
444:3596.72, 
445:3603.38, 
446:3610.04, 
447:3616.7, 
448:3623.36, 
449:3630.02, 
45:794.51, 
450:3636.68, 
451:3643.34, 
452:3650.0, 
453:3656.67, 
454:3663.33, 
455:3669.99, 
456:3676.65, 
457:3683.32, 
458:3689.98, 
459:3696.65, 
46:801.04, 
460:3703.31, 
461:3709.98, 
462:3716.64, 
463:3723.31, 
464:3729.98, 
465:3736.64, 
466:3743.31, 
467:3749.98, 
468:3756.65, 
469:3763.31, 
47:807.56, 
470:3769.98, 
471:3776.65, 
472:3783.32, 
473:3789.99, 
474:3796.66, 
475:3803.33, 
476:3810.0, 
477:3816.67, 
478:3823.35, 
479:3830.02, 
48:814.09, 
480:3836.69, 
481:3843.36, 
482:3850.04, 
483:3856.71, 
484:3863.39, 
485:3870.06, 
486:3876.73, 
487:3883.41, 
488:3890.08, 
489:3896.76, 
49:820.62, 
5:462.15, 
50:827.15, 
51:833.68, 
52:840.22, 
53:846.75, 
54:853.28, 
55:859.81, 
56:866.34, 
57:872.88, 
58:879.41, 
59:885.95, 
6:468.65, 
60:892.48, 
61:899.02, 
62:905.55, 
63:912.09, 
64:918.62, 
65:925.16, 
66:931.7, 
67:938.24, 
68:944.77, 
69:951.31, 
7:475.16, 
70:957.85, 
71:964.39, 
72:970.93, 
73:977.47, 
74:984.01, 
75:990.55, 
76:997.1, 
77:1003.64, 
78:1010.18, 
79:1047.2, 
8:481.67, 
80:1053.75, 
81:1060.3, 
82:1066.85, 
83:1073.41, 
84:1079.96, 
85:1086.51, 
86:1093.07, 
87:1099.62, 
88:1106.17, 
89:1112.73, 
9:488.17, 
90:1119.28, 
91:1125.84, 
92:1132.39, 
93:1138.95, 
94:1145.51, 
95:1152.06, 
96:1158.62, 
97:1165.18, 
98:1171.73, 
99:1178.29}

crism_wv = OrderedDict(sorted(crism_wv.items()))