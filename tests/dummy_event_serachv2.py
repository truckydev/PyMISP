evt = {
		"Event": {
			"info": "event for searchV2",
			"Attribute": [
				{"type": "user-agent", "value": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13"},
				{"type": "uri", "value": "groups/123moveis-watch-pitch-perfect-3-2017-putlocker-online-full-movies/"},
				{"type": "pattern-in-file", "value": "^.{6,30}Exif"},
				{"type": "domain", "value": "thegymsportsbars.com"},
				{"type": "domain|ip", "value": "thegymsportsbars.com|198.71.233.195"},
				{"type": "url", "value": "coinhive.com/lib/coinhive.min.js"},
				{"type": "link", "value": "https://urlquery.net/report/0438049c-5b4a-4809-bf21-caf201d5ace5"},
				{"type": "datetime", "value": "2017-12-21 15:22:42 CET"},
				{"type": "campaign-name", "value": "myDummyCampaignName"},
				{"type": "AS", "value": "ResultForAsType",
				"Tag": [{"name": "veris:action:malware:vector=\"Download by malware\""}]},
				{"type": "domain|ip",
				"category": "Network activity",
				"comment": "https:\/\/urlquery.net\/report\/0438049c-5b4a-4809-bf21-caf201d5ace5",
				"deleted": False,
				"value": "coinhive.com|94.130.90.154",
				"Tag": [
					{"name": "veris:action:malware:vector=\"Download by malware\""},
					{"name": "malware_classification:malware-category=\"Downloader\""}
				]
				}
			],
			"Galaxy": [],
			"Object": [
				{
					"name": "http-request",
					"meta-category": "network",
					"description": "A single HTTP request header",
					"template_uuid": "b4a8d163-8110-4239-bfcf-e08f3a9fdf7b",
					"template_version": "1",
					"comment": "https:\/\/urlquery.net\/report\/0438049c-5b4a-4809-bf21-caf201d5ace5",
					"ObjectReference": [
						{
							"referenced_uuid": "5a3bcee4-aba8-453d-8212-2adec183c10b",
							"referenced_id": "90961",
							"referenced_type": "0",
							"relationship_type": "related-to",
							"comment": "",
							"Attribute": {
								"type": "domain|ip",
								"category": "Network activity",
								"value": "coinhive.com|94.130.90.154"
							}
						}
					],
					"Attribute": [
						{
							"type": "text",
							"category": "Other",
							"object_relation": "text",
							"value": "Alerts:\r\n  Blacklists:\r\n    - fortinet: Malware\r\n    - malwaredomains: maliciousjs",
						},
						{
							"type": "other",
							"category": "Network activity",
							"object_relation": "content-type",
							"value": "HTTP\/1.1",
						},
						{
							"type": "hostname",
							"category": "Network activity",
							"object_relation": "host",
							"value": "coinhive.com",
						},
						{
							"type": "http-method",
							"category": "Network activity",
							"object_relation": "method",
							"value": "GET",
						},
						{
							"type": "other",
							"category": "Network activity",
							"object_relation": "referer",
							"value": "http:\/\/thegymsportsbars.com\/groups\/123moveis-watch-pitch-perfect-3-2017-putlocker-online-full-movies\/",
						},
						{
							"type": "uri",
							"category": "Network activity",
							"object_relation": "uri",
							"value": "\/lib\/coinhive.min.js",
						},
						{
							"type": "url",
							"category": "Network activity",
							"uuid": "5a3bceb1-ad30-4dae-a8b4-2addc183c10b",
							"object_relation": "url",
							"value": "coinhive.com\/lib\/coinhive.min.js",
						},
						{
							"type": "user-agent",
							"category": "Network activity",
							"object_relation": "user-agent",
							"value": "Mozilla\/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko\/20101203 Firefox\/3.6.13",
						}
					]
				},
				{
					"name": "file",
					"meta-category": "file",
					"description": "File object describing a file with meta-information",
					"template_uuid": "688c46fb-5edb-40a3-8273-1af7923e2215",
					"template_version": "7",
					"comment": "BitCoinMiner",
					"Attribute": [
						{
							"type": "md5",
							"category": "Payload delivery",
							"object_relation": "md5",
							"value": "9c1e4a824b32e15b44209fd8c1edb1f5",
						},
						{
							"type": "pattern-in-file",
							"category": "Payload installation",
							"object_relation": "pattern-in-file",
							"value": "ASCII English text, with very long lines",
						},
						{
							"type": "filename",
							"category": "Payload delivery",
							"object_relation": "filename",
							"value": "coinhive.min.js",
						},
						{
							"type": "filename",
							"category": "Payload delivery",
							"object_relation": "filename",
							"value": "javascript.js",
						},
						{
							"type": "filename",
							"category": "Payload delivery",
							"object_relation": "filename",
							"value": "ch.min.js",
						},
						{
							"type": "filename",
							"category": "Payload delivery",
							"object_relation": "filename",
							"value": "59f4729193256.min.js",
						},
						{
							"type": "filename",
							"category": "Payload delivery",
							"object_relation": "filename",
							"value": "p.txt",
						},
						{
							"type": "text",
							"category": "Other",
							"object_relation": "text",
							"value": "https:\/\/www.virustotal.com\/#\/file\/b2ba4a8bed80048b02fa1ba8befd0a5ca47f0a67c687fadd63173283cc3a957b\/details",
						},
						{
							"type": "sha1",
							"category": "Payload delivery",
							"object_relation": "sha1",
							"value": "dde80f3f5c21801edc5cb4c34f8e49f2906387f4",
						},
						{
							"type": "text",
							"category": "Other",
							"object_relation": "mimetype",
							"value": "text",
						},
						{
							"type": "size-in-bytes",
							"category": "Other",
							"object_relation": "size-in-bytes",
							"value": "136850000",
						},
						{
							"id": "90990",
							"type": "ssdeep",
							"category": "Payload delivery",
							"object_relation": "ssdeep",
							"value": "1536:8QRC73mKfdLqt31K3VfoH7ydWAYpe5t57CjwXlmNjx9Dq1FFtYi06fmwB7lyyQN5:jRK1mtCYZmFFt6gD8igBoOCI1H",
						},
						{
							"type": "text",
							"category": "Other",
							"object_relation": "state",
							"value": "Malicious",
						},
						{
							"type": "text",
							"category": "Other",
							"object_relation": "state",
							"value": "Malicious",
						}
					]
				}
			],
			"Tag": [
				{"name": "Type:OSINT"},
				{"name": "misp-galaxy:tool=\"FINSPY\""},
				{"name": "misp-galaxy:tool=\"AmmyAdmin\""},
			]
		}
	}