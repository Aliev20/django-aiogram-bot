function t_fallback__init(){t_fallback__initTags("LINK"),t_fallback__initTags("SCRIPT"),"loading"!=document.readyState?t_fallback__initTags("IMG"):document.addEventListener("DOMContentLoaded",function(){t_fallback__initTags("IMG")})}function t_fallback__initTags(a){var t=document.querySelectorAll(a);Array.prototype.forEach.call(t,function(t){"set"!==t.isReloadFuncSet&&(t.onerror=function(){t_fallback__reloadSRC(this),this.isReloadFuncSet="set"}),"y"===t.loaderr&&(t.loaderr="",t_fallback__reloadSRC(t)),"IMG"==a&&t.complete&&0===t.naturalWidth&&""!==t.src&&t_fallback__reloadSRC(t)})}function t_fallback__reloadSRC(t){"function"==typeof t_falladv__reloadSRC?t_falladv__reloadSRC(t):(t_fallback__loadAdvancedJS(),setTimeout(function(){t_fallback__reloadSRC(t)},500))}function t_fallback__handleTimeout(){"loading"==document.readyState&&"object"==typeof window.performance&&null!==document.head.querySelector('script[src^="https://static.tildacdn."]')&&(t_fallback__loadAdvancedJS(),setTimeout(function(){("function"==typeof t_falladv__handleDomTimeOut?t_falladv__handleDomTimeOut:t_fallback__handleTimeout)()},500))}function t_fallback__loadAdvancedJS(){var a;!0!==window.t_isfalladvstartload&&(window.t_isfalladvstartload=!0,(a=new XMLHttpRequest).open("GET","https://stat.tildacdn.com/js/tilda-fallback-advanced-1.0.min.js",!0),a.onreadystatechange=function(){var t;4==a.readyState&&200==a.status&&((t=document.createElement("script")).innerHTML=a.responseText,document.head.appendChild(t))},a.send())}t_fallback__init(),document.addEventListener("DOMContentLoaded",t_fallback__init),setTimeout(t_fallback__handleTimeout,3e4),setTimeout(function(){var t=document.getElementById("allrecords");t&&!t.classList.contains("t-records_animated")&&((t=document.createElement("style")).type="text/css",t.innerHTML="div.t-records {opacity: 1;}",document.getElementsByTagName("head")[0].appendChild(t))},5e3);