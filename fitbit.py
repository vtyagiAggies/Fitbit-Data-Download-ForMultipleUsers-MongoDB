



<!DOCTYPE html>
<html lang="en" class=" is-copy-enabled is-u2f-enabled">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=1020">
    
    
    <title>FitBit-Group-Data-Downloader/fitbit.py at master · rhavasy/FitBit-Group-Data-Downloader</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="rhavasy/FitBit-Group-Data-Downloader" name="twitter:title" /><meta content="FitBit-Group-Data-Downloader - FitBit Python Library" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/3180180?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/3180180?v=3&amp;s=400" property="og:image" /><meta content="rhavasy/FitBit-Group-Data-Downloader" property="og:title" /><meta content="https://github.com/rhavasy/FitBit-Group-Data-Downloader" property="og:url" /><meta content="FitBit-Group-Data-Downloader - FitBit Python Library" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MTIxODM2NDU6NGIwOThmYTE1ZGFlYTA1OWFiNGM3Mzc0ZDYwOGNmNTg6YWYwYWNkMTMwYThmNjYxODVlNjIxNTgxNjU3NzBkZjkxMDhjODYzYzkwN2YyZjcyNzAxNmFjOTIwMTBiNGU0Mw==--bb09d8d892905c7317a8ba518b52d6d12a7623d1">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="A55B0C08:35C8:6DE8D17:5671F9E1" name="octolytics-dimension-request_id" /><meta content="12183645" name="octolytics-actor-id" /><meta content="vtyagiAggies" name="octolytics-actor-login" /><meta content="ed14738717e74d8905f1638b7d10d2fd2cf2974b5398bca9b6554ee8bcba065d" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />
<meta content="Rails, view, blob#show" data-pjax-transient="true" name="analytics-event" />


  <meta class="js-ga-set" name="dimension1" content="Logged In">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="vtyagiAggies">

        <meta name="expected-hostname" content="github.com">

      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta content="b50005ed8523b5d7af97ed66dd1444724135f239" name="form-nonce" />

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-502ab50993b65c1ac75efa286ffd5304245f6c9bb4171ac014fbcf92f6f688de.css" integrity="sha256-UCq1CZO2XBrHXvoob/1TBCRfbJu0FxrAFPvPkvb2iN4=" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github2-3489439d0b3b87d58adb9528029812d8b7ab444fc86a839d940dc1228f09c653.css" integrity="sha256-NIlDnQs7h9WK25UoApgS2LerRE/IaoOdlA3BIo8JxlM=" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="4a30b736c76385e3865be28e53dfda2b">

      
  <meta name="description" content="FitBit-Group-Data-Downloader - FitBit Python Library">
  <meta name="go-import" content="github.com/rhavasy/FitBit-Group-Data-Downloader git https://github.com/rhavasy/FitBit-Group-Data-Downloader.git">

  <meta content="3180180" name="octolytics-dimension-user_id" /><meta content="rhavasy" name="octolytics-dimension-user_login" /><meta content="7900477" name="octolytics-dimension-repository_id" /><meta content="rhavasy/FitBit-Group-Data-Downloader" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="4401002" name="octolytics-dimension-repository_parent_id" /><meta content="jflasher/FitBit.py" name="octolytics-dimension-repository_parent_nwo" /><meta content="2068642" name="octolytics-dimension-repository_network_root_id" /><meta content="jplattel/FitBit.py" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/rhavasy/FitBit-Group-Data-Downloader/commits/master.atom" rel="alternate" title="Recent Commits to FitBit-Group-Data-Downloader:master" type="application/atom+xml">

  </head>


  <body class="logged_in   env-production linux vis-public fork page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/rhavasy/FitBit-Group-Data-Downloader/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/rhavasy/FitBit-Group-Data-Downloader/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      aria-label="Search this repository"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
      <span class="js-socket-channel js-updatable-content"
        data-channel="notification-changed:vtyagiAggies"
        data-url="/notifications/header">
      <a href="/notifications" aria-label="You have unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
          <span class="mail-status unread"></span>
          <span class="octicon octicon-bell"></span>
</a>  </span>

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus left"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>


  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="rhavasy/FitBit-Group-Data-Downloader">This repository</span>
  </div>
    <a class="dropdown-item" href="/rhavasy/FitBit-Group-Data-Downloader/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/vtyagiAggies"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@vtyagiAggies" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/12183645?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu  dropdown-menu-sw">
        <div class=" dropdown-header header-nav-current-user css-truncate">
            Signed in as <strong class="css-truncate-target">vtyagiAggies</strong>

        </div>


        <div class="dropdown-divider"></div>

          <a class="dropdown-item" href="/vtyagiAggies" data-ga-click="Header, go to profile, text:your profile">
            Your profile
          </a>
        <a class="dropdown-item" href="/stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
          <a class="dropdown-item" href="/integrations" data-ga-click="Header, go to integrations, text:integrations">
            Integrations
          </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>

          <div class="dropdown-divider"></div>

          <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
            Settings
          </a>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="b50005ed8523b5d7af97ed66dd1444724135f239" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="zKkOyS+9fhOr0LwZu7ZtYjlm/rXc4It7P2E2z8QrEUJhKiAWr6X9RgUWausAI+jbU4OnhkF7zHsKfy5akqMPzw==" /></div>
            <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
              Sign out
            </button>
</form>
      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>

      

      


    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main" class="main-content">
        <div itemscope itemtype="http://schema.org/WebPage">
    <div id="js-repo-pjax-container" class="context-loader-container js-repo-nav-next" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="b50005ed8523b5d7af97ed66dd1444724135f239" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="N/juCIpxDZ0olxiXpId9QWnJgQ5SkpJrGd/UOqbRyPVu8gkfph8mNddoWWyAHKRyAPoWsi3JGYOB3ymbl9RidA==" /></div>      <input id="repository_id" name="repository_id" type="hidden" value="7900477" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/rhavasy/FitBit-Group-Data-Downloader/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
              <span class="octicon octicon-eye"></span>
              Watch
            </span>
          </a>
          <a class="social-count js-social-count" href="/rhavasy/FitBit-Group-Data-Downloader/watchers">
            4
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-eye"></span>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-eye"></span>
                      Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-mute"></span>
                      Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container on">

    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/rhavasy/FitBit-Group-Data-Downloader/unstar" class="js-toggler-form starred js-unstar-button" data-form-nonce="b50005ed8523b5d7af97ed66dd1444724135f239" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="mN15LhNxGJj4lV7CJ41DDXBPcKntWRwsIbsvDmwerdt39Vl4/JKw1W74jZyzo/6DUvy3KUFjZ3Wqi8kCH/Uldg==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar rhavasy/FitBit-Group-Data-Downloader"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/rhavasy/FitBit-Group-Data-Downloader/stargazers">
          6
        </a>
</form>
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/rhavasy/FitBit-Group-Data-Downloader/star" class="js-toggler-form unstarred js-star-button" data-form-nonce="b50005ed8523b5d7af97ed66dd1444724135f239" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="GCd650ap6eYSeH4Bk5NJRFMb8g1knqV+W3GFx3XfFcutR+6BkuMTRf4pr+p8W05YTGkne5FPNGMbuOtY45NBlA==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star rhavasy/FitBit-Group-Data-Downloader"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/rhavasy/FitBit-Group-Data-Downloader/stargazers">
          6
        </a>
</form>  </div>

  </li>

  <li>
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/rhavasy/FitBit-Group-Data-Downloader/fork" class="btn-with-count" data-form-nonce="b50005ed8523b5d7af97ed66dd1444724135f239" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="G0NwD8SGR0MxyQplNYs608Un4dBfCxIOpQIRdgKzhyiCNdjh0J7ok6GNnb6EbMEvmEdaSNECtv20G0cz42G6wg==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of rhavasy/FitBit-Group-Data-Downloader to your account"
                aria-label="Fork your own copy of rhavasy/FitBit-Group-Data-Downloader to your account">
              <span class="octicon octicon-repo-forked"></span>
              Fork
            </button>
</form>
    <a href="/rhavasy/FitBit-Group-Data-Downloader/network" class="social-count">
      22
    </a>
  </li>
</ul>

    <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public ">
  <span class="octicon octicon-repo-forked"></span>
  <span class="author"><a href="/rhavasy" class="url fn" itemprop="url" rel="author"><span itemprop="title">rhavasy</span></a></span><!--
--><span class="path-divider">/</span><!--
--><strong><a href="/rhavasy/FitBit-Group-Data-Downloader" data-pjax="#js-repo-pjax-container">FitBit-Group-Data-Downloader</a></strong>

  <span class="page-context-loader">
    <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
  </span>

    <span class="fork-flag">
      <span class="text">forked from <a href="/jflasher/FitBit.py">jflasher/FitBit.py</a></span>
    </span>
</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <a href="/rhavasy/FitBit-Group-Data-Downloader" aria-label="Code" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /rhavasy/FitBit-Group-Data-Downloader">
    <span class="octicon octicon-code"></span>
    Code
</a>
    <a href="/rhavasy/FitBit-Group-Data-Downloader/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /rhavasy/FitBit-Group-Data-Downloader/issues">
      <span class="octicon octicon-issue-opened"></span>
      Issues
      <span class="counter">8</span>
</a>
  <a href="/rhavasy/FitBit-Group-Data-Downloader/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /rhavasy/FitBit-Group-Data-Downloader/pulls">
    <span class="octicon octicon-git-pull-request"></span>
    Pull requests
    <span class="counter">0</span>
</a>
    <a href="/rhavasy/FitBit-Group-Data-Downloader/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /rhavasy/FitBit-Group-Data-Downloader/wiki">
      <span class="octicon octicon-book"></span>
      Wiki
</a>
  <a href="/rhavasy/FitBit-Group-Data-Downloader/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /rhavasy/FitBit-Group-Data-Downloader/pulse">
    <span class="octicon octicon-pulse"></span>
    Pulse
</a>
  <a href="/rhavasy/FitBit-Group-Data-Downloader/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /rhavasy/FitBit-Group-Data-Downloader/graphs">
    <span class="octicon octicon-graph"></span>
    Graphs
</a>

</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/rhavasy/FitBit-Group-Data-Downloader/blob/d58a25a1fc97f7ddf5bbd674946505ef4e9e5db2/fitbit.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:cebf788b469ba1ed8e040d9f1a4c1e91 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    title="master"
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/rhavasy/FitBit-Group-Data-Downloader/blob/added-new-API-calls/fitbit.py"
               data-name="added-new-API-calls"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="added-new-API-calls">
                added-new-API-calls
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/rhavasy/FitBit-Group-Data-Downloader/blob/gh-pages/fitbit.py"
               data-name="gh-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="gh-pages">
                gh-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/rhavasy/FitBit-Group-Data-Downloader/blob/master/fitbit.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/rhavasy/FitBit-Group-Data-Downloader/find/master"
          class="js-show-file-finder btn btn-sm"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/rhavasy/FitBit-Group-Data-Downloader" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">FitBit-Group-Data-Downloader</span></a></span></span><span class="separator">/</span><strong class="final-path">fitbit.py</strong>
  </div>
</div>

<include-fragment class="commit-tease" src="/rhavasy/FitBit-Group-Data-Downloader/contributors/master/fitbit.py">
  <div>
    Fetching contributors&hellip;
  </div>

  <div class="commit-tease-contributors">
    <img alt="" class="loader-loading left" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" />
    <span class="loader-error">Cannot retrieve contributors at this time</span>
  </div>
</include-fragment>
<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="btn-group">
      <a href="/rhavasy/FitBit-Group-Data-Downloader/raw/master/fitbit.py" class="btn btn-sm " id="raw-url">Raw</a>
        <a href="/rhavasy/FitBit-Group-Data-Downloader/blame/master/fitbit.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
      <a href="/rhavasy/FitBit-Group-Data-Downloader/commits/master/fitbit.py" class="btn btn-sm " rel="nofollow">History</a>
    </div>


        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/rhavasy/FitBit-Group-Data-Downloader/edit/master/fitbit.py" class="inline-form js-update-url-with-hash" data-form-nonce="b50005ed8523b5d7af97ed66dd1444724135f239" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="UMgkOY5sKq1/mCE3+uQ5keQzTBeHmOfM3KjGG9xXCIU0DE0n38LxxEKFbb1EgmkdVlZoTZp4N59bcN2ShNwdJw==" /></div>
          <button class="octicon-btn tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
            <span class="octicon octicon-pencil"></span>
          </button>
</form>        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/rhavasy/FitBit-Group-Data-Downloader/delete/master/fitbit.py" class="inline-form" data-form-nonce="b50005ed8523b5d7af97ed66dd1444724135f239" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ka9Eeuab47ZgsfaUOFtUWbLTPPyVQU8AjKK06WG0ZgQsg1mzcg8HnL9GY4Siiot/ZcFoYbvKMU260JB+9tAW4w==" /></div>
          <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <span class="octicon octicon-trashcan"></span>
          </button>
</form>  </div>

  <div class="file-info">
      104 lines (95 sloc)
      <span class="file-info-divider"></span>
    6.08 KB
  </div>
</div>

  

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-s">A Python library for accessing the FitBit API.</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-s">This library provides a wrapper to the FitBit API and does not provide storage of tokens or caching if that is required.</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Most of the code has been adapted from: https://groups.google.com/group/fitbit-api/browse_thread/thread/0a45d0ebed3ebccb</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> httplib, time, ConfigParser, sys</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> oauth2 <span class="pl-k">as</span> oauth</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">FitBit</span>():</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#Read global values from config file</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">    config <span class="pl-k">=</span> ConfigParser.RawConfigParser()</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">        cf<span class="pl-k">=</span><span class="pl-c1">open</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>fitbit_config.ini<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">IOError</span>:</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">        sys.exit(<span class="pl-s"><span class="pl-pds">&quot;</span>Missing or corrupt fitbit_config.ini file in program path! Terminating execution.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">    config.readfp(cf)</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">    cf.close()</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">    APP_NAME <span class="pl-k">=</span> config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>Globals<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>AppName<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    CONSUMER_KEY <span class="pl-k">=</span> config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>Globals<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>ConsumerKey<span class="pl-pds">&#39;</span></span>) </td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">    CONSUMER_SECRET <span class="pl-k">=</span> config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>Globals<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>ConsumerSecret<span class="pl-pds">&#39;</span></span>) </td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">    SERVER <span class="pl-k">=</span> config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>Globals<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Server<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    REQUEST_TOKEN_URL <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-c1">%s</span>/oauth/request_token<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> SERVER </td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">    ACCESS_TOKEN_URL <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-c1">%s</span>/oauth/access_token<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> SERVER </td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    AUTHORIZATION_URL <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-c1">%s</span>/oauth/authorize<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> SERVER</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">    TOKENFILENAME <span class="pl-k">=</span> config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>FileData<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>OutputFilePrefix<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">FetchResponse</span>(<span class="pl-smi">self</span>, <span class="pl-smi">oauth_request</span>, <span class="pl-smi">connection</span>, <span class="pl-smi">url</span>): <span class="pl-c">#added URL as config. parameter</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">        connection.request(oauth_request.method, url, <span class="pl-smi">headers</span><span class="pl-k">=</span>oauth_request.to_header()) <span class="pl-c">#added headers to pass parameters</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">        response <span class="pl-k">=</span> connection.getresponse()</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">        s<span class="pl-k">=</span>response.read()</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> s</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">GetRequestToken</span>(<span class="pl-smi">self</span>): </td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">        connection <span class="pl-k">=</span> httplib.HTTPSConnection(<span class="pl-v">self</span>.SERVER)</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">        consumer <span class="pl-k">=</span> oauth.Consumer(<span class="pl-v">self</span>.CONSUMER_KEY, <span class="pl-v">self</span>.CONSUMER_SECRET)</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">        signature_method <span class="pl-k">=</span> oauth.SignatureMethod_PLAINTEXT()</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">        oauth_request <span class="pl-k">=</span> oauth.Request.from_consumer_and_token(consumer, <span class="pl-smi">http_url</span><span class="pl-k">=</span><span class="pl-v">self</span>.REQUEST_TOKEN_URL)</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">        oauth_request.sign_request(signature_method, consumer, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">        resp <span class="pl-k">=</span> <span class="pl-v">self</span>.FetchResponse(oauth_request, connection, <span class="pl-v">self</span>.REQUEST_TOKEN_URL) <span class="pl-c">#passing in explicit url</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">        auth_token <span class="pl-k">=</span> oauth.Token.from_string(resp) </td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">        auth_url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>?oauth_token=<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (<span class="pl-v">self</span>.AUTHORIZATION_URL, auth_token.key) <span class="pl-c">#build the URL</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> auth_url, auth_token</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">   </td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">GetAccessToken</span>(<span class="pl-smi">self</span>, <span class="pl-smi">access_code</span>, <span class="pl-smi">auth_token</span>):</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">        oauth_verifier <span class="pl-k">=</span> access_code</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        connection <span class="pl-k">=</span> httplib.HTTPSConnection(<span class="pl-v">self</span>.SERVER) </td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">        consumer <span class="pl-k">=</span> oauth.Consumer(<span class="pl-v">self</span>.CONSUMER_KEY, <span class="pl-v">self</span>.CONSUMER_SECRET) </td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">        signature_method <span class="pl-k">=</span> oauth.SignatureMethod_PLAINTEXT()</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">        oauth_request <span class="pl-k">=</span> oauth.Request.from_consumer_and_token(consumer, <span class="pl-smi">token</span><span class="pl-k">=</span>auth_token, <span class="pl-smi">http_url</span><span class="pl-k">=</span><span class="pl-v">self</span>.ACCESS_TOKEN_URL, <span class="pl-smi">parameters</span><span class="pl-k">=</span>{<span class="pl-s"><span class="pl-pds">&#39;</span>oauth_verifier<span class="pl-pds">&#39;</span></span>: oauth_verifier})</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">        oauth_request.sign_request(signature_method, consumer, auth_token)</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># now the token we get back is an access token</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">        access_token <span class="pl-k">=</span> oauth.Token.from_string(<span class="pl-v">self</span>.FetchResponse(oauth_request,connection, <span class="pl-v">self</span>.ACCESS_TOKEN_URL)) <span class="pl-c"># parse the response into an OAuthToken object / passingin explicit url</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># store the access token when returning it</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">        access_token <span class="pl-k">=</span> access_token.to_string()</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> access_token</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">   </td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">ApiCall</span>(<span class="pl-smi">self</span>, <span class="pl-smi">access_token</span>, <span class="pl-smi">apiCall</span>): <span class="pl-c">#removed original hardcoded api call in favor of string passed from PickApiCall()</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">        signature_method <span class="pl-k">=</span> oauth.SignatureMethod_PLAINTEXT()</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">        connection <span class="pl-k">=</span> httplib.HTTPSConnection(<span class="pl-v">self</span>.SERVER) </td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#build the access token from a string</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">        access_token <span class="pl-k">=</span> oauth.Token.from_string(access_token)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">        consumer <span class="pl-k">=</span> oauth.Consumer(<span class="pl-v">self</span>.CONSUMER_KEY, <span class="pl-v">self</span>.CONSUMER_SECRET)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">        final_url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-v">self</span>.SERVER <span class="pl-k">+</span> apiCall</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">        oauth_request <span class="pl-k">=</span> oauth.Request.from_consumer_and_token(consumer, <span class="pl-smi">token</span><span class="pl-k">=</span>access_token, <span class="pl-smi">http_url</span><span class="pl-k">=</span>final_url)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">        oauth_request.sign_request(signature_method, consumer, access_token)</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> oauth_request.to_header(<span class="pl-smi">realm</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>api.fitbit.com<span class="pl-pds">&#39;</span></span>) </td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">        connection.request(<span class="pl-s"><span class="pl-pds">&#39;</span>GET<span class="pl-pds">&#39;</span></span>, apiCall, <span class="pl-smi">headers</span><span class="pl-k">=</span>headers) </td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        resp <span class="pl-k">=</span> connection.getresponse() </td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        response <span class="pl-k">=</span> resp.read() </td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> response</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">PickApiCall</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Presents user with options and returns specific FitBit API string selected as a string. See FitBit API docs for specific call syntax.<span class="pl-pds">&quot;&quot;&quot;</span></span>      </td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">        calls <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>/1/user/-/profile.xml<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/1/user/-/devices.xml<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>/1/user/-/activities/steps/date/today/7d.xml<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>built dynamically<span class="pl-pds">&#39;</span></span>] <span class="pl-c"># profile data, device data, last 7 days steps</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">        desc <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>User profile data.<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Device data (incl. last upload).<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Last 7 days<span class="pl-cce">\&#39;</span> steps.<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Steps for specific date range.<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>(desc)):</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">            e <span class="pl-k">=</span> desc[i]</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%i</span>. <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (i<span class="pl-k">+</span><span class="pl-c1">1</span>, e) <span class="pl-c"># i+1 makes the list appear 1,2,3 to user rather than 0-based index </span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">        prompt <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-c1">True</span>: <span class="pl-c">#ensures integer is selected</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">                prompt <span class="pl-k">=</span> <span class="pl-c1">int</span>(<span class="pl-c1">raw_input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Select an API call by number:<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">int</span>(prompt) <span class="pl-k">&lt;</span> <span class="pl-c1">1</span> <span class="pl-k">or</span> <span class="pl-c1">int</span>(prompt) <span class="pl-k">&gt;</span> <span class="pl-c1">len</span>(desc):</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Invalid selection. Last 7 days steps selected by default.<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">                    prompt <span class="pl-k">=</span> <span class="pl-c1">3</span> <span class="pl-c">#if out of bounds default to last 7 days data</span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Please select a valid number from the list. Try again ...<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> prompt <span class="pl-k">==</span> <span class="pl-c1">4</span>: <span class="pl-c"># Should change this to verify string rather than index in case list changes.</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>: <span class="pl-c">#Checks is string can be formatted as a time - ie is it in correct format</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">                    startdate <span class="pl-k">=</span> time.strptime(<span class="pl-c1">raw_input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Enter desired start date (mm/dd/yyyy): <span class="pl-pds">&#39;</span></span>), <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%m</span>/<span class="pl-c1">%d</span>/<span class="pl-c1">%Y</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">                    enddate <span class="pl-k">=</span> time.strptime(<span class="pl-c1">raw_input</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>Enter desired end date (mm/dd/yyyy): <span class="pl-pds">&#39;</span></span>), <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%m</span>/<span class="pl-c1">%d</span>/<span class="pl-c1">%Y</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c">#THIS TEST REFORMATS startdate &amp; enddate AS A struc_time OBJECT. MUST CONVERT BACK TO STRING FOR USE IN API CALL.</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Entered date does not match mm/dd/yyyy format. Try again.<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">            apistring <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/1/user/-/activities/steps/date/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> time.strftime(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%Y</span>-<span class="pl-c1">%m</span>-<span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span>,startdate) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> time.strftime(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%Y</span>-<span class="pl-c1">%m</span>-<span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span>,enddate) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>.xml<span class="pl-pds">&#39;</span></span> <span class="pl-c">#time.strftime converts struc_time back to string in proper format</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">            apistring <span class="pl-k">=</span> calls[<span class="pl-c1">int</span>(prompt)<span class="pl-k">-</span><span class="pl-c1">1</span>] <span class="pl-c"># -1 brings the chosen base-1 index back to base-0 of list</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> apistring</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop"></div>
</div>

    </div>
  </div>

    </div>

        <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
        <li><a href="https://github.com/pricing" data-ga-click="Footer, go to pricing, text:pricing">Pricing</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.09243s from github-fe127-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    
    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <span class="octicon octicon-x"></span>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" integrity="sha256-7460qJ7p88i3YTMH/liaj1cFgX987ie+xRzl6WMjSr8=" src="https://assets-cdn.github.com/assets/frameworks-ef8eb4a89ee9f3c8b7613307fe589a8f5705817f7cee27bec51ce5e963234abf.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-QQ/fyDvlG8+ub5XjaMUJm15L2Hf78jJjgj3I9Vybb4Y=" src="https://assets-cdn.github.com/assets/github-410fdfc83be51bcfae6f95e368c5099b5e4bd877fbf23263823dc8f55c9b6f86.js"></script>
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <span class="octicon octicon-alert"></span>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
  </body>
</html>

